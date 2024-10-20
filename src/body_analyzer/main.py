from flask import Flask

from src.body_analyzer.endpoints import configure_routes

app = Flask(__name__)

for rule in app.url_map.iter_rules():
    print(rule)

# Llama a la función para configurar las rutas
configure_routes(app)

# Imprimir las rutas registradas
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
