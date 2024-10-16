# Define the name of your virtual environment
VENV_NAME = .venv

# Paths to activate virtual environment and Python
VENV_ACTIVATE = $(VENV_NAME)/bin/activate
PYTHON_PATH = $(shell which python3.12)

# Project name
PROJECT_NAME = body_analyzer

# Add the virtual environment's bin directory to PATH
export PATH := /app/.local/bin:$(PATH)

# Create virtual environment
create-venv: delete-venv
	$(PYTHON_PATH) -m venv $(VENV_NAME)

# Delete virtual environment
delete-venv:
	rm -rf $(VENV_NAME)

# Uninstall project
uninstall:
	$(VENV_NAME)/bin/pip uninstall -y $(PROJECT_NAME)

# Build project
build: update-pip
	$(PYTHON_PATH) setup.py sdist bdist_wheel

# Clean project directories
clean:
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Reinstall dependencies
reinstall-dependencies: update-pip delete-dependencies install-dep clean

# Update pip
update-pip:
	$(VENV_NAME)/bin/pip install --upgrade pip

# Delete all installed dependencies
delete-dependencies:
	$(VENV_NAME)/bin/pip freeze | xargs $(VENV_NAME)/bin/pip uninstall -y

# Install Docker in the virtual environment
docker:
	$(VENV_NAME)/bin/pip install docker

# Install project dependencies
install-dep:
	$(VENV_NAME)/bin/pip install -e .

# Run the Flask application
run:
	FLASK_APP=src/body_analyzer/main.py $(VENV_NAME)/bin/python -m flask run

# Run tests
test: ## Run tests
	$(VENV_NAME)/bin/python -m unittest discover -s tests

# Install coverage
install-coverage:
	$(VENV_NAME)/bin/pip install coverage

# Run tests with coverage
coverage: install-coverage
	$(VENV_NAME)/bin/coverage run --source=src/body_analyzer -m unittest discover -s tests -p "test_*.py"
	$(VENV_NAME)/bin/coverage report
	$(VENV_NAME)/bin/coverage html


# Clean coverage files
clean-coverage:
	rm -rf .coverage htmlcov