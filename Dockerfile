# Usa una imagen base de Python
FROM python:3.11-slim

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY pyproject.toml .
COPY README.md .
COPY src/ ./src

# Instala las herramientas de construcción necesarias
RUN apt-get update && apt-get install -y build-essential
RUN pip install prometheus_flask_exporter

# Actualiza pip e instala las dependencias
RUN python -m pip install --upgrade pip && \
    pip install setuptools wheel && \
    pip install . gunicorn

# Define la variable de entorno FLASK_APP
ENV FLASK_APP=src/body_analyzer/main.py

# Expón el puerto de Flask (por defecto 5000)
EXPOSE 5000

# Ejecuta Gunicorn como el servidor de producción
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.body_analyzer.main:app"]
