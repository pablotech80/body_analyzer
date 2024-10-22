import flask

from src.body_analyzer.constantes import *
from src.body_analyzer.endpoints import configure_routes

app = flask.Flask(__name__)

# Llama a la función para configurar las rutas
configure_routes(app)

# Imprimir las rutas registradas
for rule in app.url_map.iter_rules():
    print(rule)

if __name__ == "__main__":
    app.run(debug=True)
