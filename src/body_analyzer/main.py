from flask import Flask, request, jsonify
from calculos import calcular_porcentaje_grasa, calcular_tmb

app = Flask(__name__)
print(app.url_map)

@app.route('/')
def home():
    return "Bienvenido a la API de Análisis de Composición Corporal by CoachBodyFit."

@app.route('/calcular_porcentaje_grasa', methods=['POST'])
def calcular_grasa_endpoint():
    data = request.get_json()
    cintura = data['cintura']
    cadera = data['cadera']
    cuello = data['cuello']
    altura = data['altura']
    genero = data['genero']

    try:
        resultado = calcular_porcentaje_grasa(cintura, cadera, cuello, altura, genero)
        return jsonify({"porcentaje_grasa": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/calcular_tmb', methods=['POST'])
def calcular_tmb_endpoint():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']
    edad = data['edad']
    genero = data['genero']

    try:
        resultado = calcular_tmb(peso, altura, edad, genero)
        return jsonify({"tmb": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400



if __name__ == '__main__':
    app.run(debug=True)
