import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a la API de Análisis de Composición Corporal by CoachBodyFit."


if __name__ == '__main__':
    app.run(debug=True)
