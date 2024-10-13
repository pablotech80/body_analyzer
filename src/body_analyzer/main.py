from flask import Flask, request, jsonify

from calculos import calcular_porcentaje_grasa, calcular_tmb, calcular_imc, calcular_agua_total

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

    if None in (cintura, cadera, cuello, altura, genero):
        return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

    try:
        resultado = calcular_porcentaje_grasa(cintura, cadera, cuello, altura, genero)
        return jsonify({"porcentaje_grasa": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    resultado_formateado = f'{resultado:.2f}' # TODO: este codigo nunca se alcanza tiene todo return antes
    return jsonify({"resultado": resultado_formateado})

@app.route('/calcular_tmb', methods=['POST'])
def calcular_tmb_endpoint():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']
    edad = data['edad']
    genero = data['genero']

    if None in (peso, altura, edad, genero):
        return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

    try:
        resultado = calcular_tmb(peso, altura, edad, genero)
        return jsonify({"tmb": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    resultado_formateado = f'{resultado:.2f}' # TODO: este codigo nunca se alcanza tiene todo return antes
    return jsonify({"resultado": resultado_formateado})

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc_endpoint():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']

    if None in (peso, altura):
        return jsonify({'error': 'Faltan parámetros obligatorios separados por coma'}), 400

    try:
        resultado = calcular_imc(peso, altura)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"imc": resultado})

@app.route('/calcular_agua_total', methods=['POST'])
def calcular_agua_total_endpoint():
    data = request.get_json()
    peso = data['peso']
    altura = data['altura']
    edad = data['edad']
    genero = data['genero']

    if None in (peso, altura, edad, genero):
        return jsonify({'error': 'Faltan párametros obligatorios'}), 400

    try:
        resultado = calcular_agua_total(peso, altura, edad, genero)
        return jsonify({"agua_total": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    resultado_formateado = f'{resultado:.2f}' # TODO: este codigo nunca se alcanza tiene todo return antes
    return jsonify({"agua_total": resultado_formateado})


if __name__ == '__main__':
    app.run(debug=True)
