export PATH := /app/.local/bin:$(PATH)
VENV_NAME?=venv
VENV_ACTIVATE=$(VENV_NAME)/bin/activate
PYTHON_PATH=$(shell which python3.11)

create-venv: delete-venv
	# TODO: Create a virtual environment

delete-venv:
	# TODO: Delete the virtual environment

uninstall:
	# TODO: Uninstall the project

build: update-pip
	# TODO: Build the project and create a distribution

clean :
	# TODO: Clean the project

reinstall-dependencies: update-pip delete-dependencies install-dep clean

update-pip:
	# TODO: Update pip

delete-dependencies:
	# TODO: Uninstall all packages and dependencies

docker:
	# TODO: Install dependencies


install-dep:
	# TODO: Install dependencies

test:		## Run tests
	#  TODO: how to run unittests

