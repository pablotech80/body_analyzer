# Define el nombre de tu entorno virtual
VENV_NAME = .venv

# Rutas de activación de entorno virtual y Python
VENV_ACTIVATE = $(VENV_NAME)/bin/activate
PYTHON_PATH = $(shell which python3.13)

# Nombre del proyecto
PROJECT_NAME = body_analyzer

# Añadir el directorio bin del entorno virtual a PATH
export PATH := /app/.local/bin:$(PATH)

# Crear entorno virtual
create-venv: delete-venv
	$(PYTHON_PATH) -m venv $(VENV_NAME)

# Eliminar entorno virtual
delete-venv:
	rm -rf $(VENV_NAME)

# Desinstalar proyecto
uninstall:
	$(VENV_NAME)/bin/pip uninstall -y $(PROJECT_NAME)

# Construir proyecto
build: update-pip
	$(PYTHON_PATH) setup.py sdist bdist_wheel

# Limpiar directorios del proyecto
clean:
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

# Reinstalar dependencias
reinstall-dependencies: update-pip delete-dependencies install-dep clean

# Actualizar pip
update-pip:
	$(VENV_NAME)/bin/pip install --upgrade pip

# Eliminar todas las dependencias instaladas
delete-dependencies:
	$(VENV_NAME)/bin/pip freeze | xargs $(VENV_NAME)/bin/pip uninstall -y

# Instalar Docker en el entorno virtual
docker:
	$(VENV_NAME)/bin/pip install docker

# Instalar dependencias del proyecto
install-dep:
	$(VENV_NAME)/bin/pip install -e .

# Ejecutar la aplicación Flask (ajustado para Docker)
run:
	@if [ -d "$(VENV_NAME)" ]; then \
		FLASK_APP=src/body_analyzer/main.py $(VENV_NAME)/bin/python -m flask run --host=0.0.0.0 --port=5000; \
	else \
		FLASK_APP=src/body_analyzer/main.py python -m flask run --host=0.0.0.0 --port=5000; \
	fi

# Ejecutar pruebas
test:
	$(VENV_NAME)/bin/python -m unittest discover -s tests
