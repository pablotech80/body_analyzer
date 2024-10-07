export PATH := /app/.local/bin:$(PATH)
VENV_NAME?=venv
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON_PATH=$(shell which python3.12)

PROJECT_NAME = body_analyzer

create-venv: delete-venv
	$(PYTHON_PATH) -m venv $(VENV_NAME)


delete-venv:
	rm -rf $(VENV_NAME)


uninstall:
	pip uninstall -y $(PROJECT_NAME)


build: update-pip
	$(PYTHON_PATH) setup.py sdist bdist_wheel


clean :
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete


reinstall-dependencies: update-pip delete-dependencies install-dep clean

update-pip:
		./${VENV_NAME}/bin/pip install --upgrade pip


delete-dependencies:
	$(VENV_NAME)/bin/pip freeze | xargs $(VENV_NAME)/bin/pip uninstall -y


docker:
	$(VENV_NAME)/bin/pip install docker



docker:
	$(VENV_NAME)/bin/pip install docker



install-dep:
	$(VENV_NAME)/bin/pip install -e .


test: ## Run tests
	$(VENV_NAME)/bin/python -m unittest discover -s tests


