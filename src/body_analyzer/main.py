from flask import Flask

app = Flask(__name__)
print(app.url_map)


@app.route("/")
def home():
    return "Bienvenido a la API de Análisis de Composición Corporal by CoachBodyFit."


if __name__ == "__main__":
    app.run(debug=True)
