export PATH := /app/.local/bin:$(PATH)
VENV_NAME?=venv
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON_PATH=$(shell which python3.12)

# export permite que todos los archivos ejecutables estén disponibles.
PROJECT_NAME = body_analyzer

create-venv: delete-venv
	$(PYTHON_PATH) -m venv $(VENV_NAME)
	# TODO: Create a virtual environment

delete-venv:
	rm -rf $(VENV_NAME)
	# TODO: Delete the virtual environment

uninstall:
	pip uninstall -y $(PROJECT_NAME)
	# TODO: Uninstall the project

build: update-pip
	$(PYTHON_PATH) setup.py sdist bdist_wheel
	# TODO: Build the project and create a distribution

clean :
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	# TODO: Clean the project

reinstall-dependencies: update-pip delete-dependencies install-dep clean

update-pip:
		./${VENV_NAME}/bin/pip install --upgrade pip


delete-dependencies:
	$(VENV_NAME)/bin/pip freeze | xargs $(VENV_NAME)/bin/pip uninstall -y
	# TODO: Uninstall all packages and dependencies

docker:
	$(VENV_NAME)/bin/pip install docker
	# TODO: Install dependencies


install-dep:
	$(VENV_NAME)/bin/pip install -e .
	# TODO: Install dependencies

test: ## Run tests
	$(VENV_NAME)/bin/python -m unittest discover -s tests

	#  TODO: how to run unittests

