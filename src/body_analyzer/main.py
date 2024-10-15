from flask import Flask, request, jsonify

from calculos import (calcular_porcentaje_grasa, calcular_tmb, calcular_imc, calcular_agua_total,
                      calcular_peso_saludable, calcular_sobrepeso, calcular_rcc)

app = Flask(__name__)
print(app.url_map)


@app.route('/')
def home():
    return "Bienvenido a la API de Análisis de Composición Corporal by CoachBodyFit."


@app.route('/calcular_porcentaje_grasa', methods=['POST'])
def calcular_grasa_endpoint():
    """
    Endpoint para calcular el porcentaje de grasa corporal.

    Args (JSON):
        cintura (float): Medida de la cintura en centímetros.
        cadera (float): Medida de la cadera en centímetros.
        cuello (float): Medida del cuello en centímetros.
        altura (float): Altura del usuario en centímetros.
        genero (str): Género del usuario ('h' para hombre, 'm' para mujer).

    Returns:
        JSON: Porcentaje de grasa corporal calculado o un mensaje de error.
    """
    try:
        # Obtener datos de la solicitud
        data = request.get_json()

        if data is None:
            return jsonify({'error': 'No se recibieron datos en la solicitud'}), 400

        cintura = data.get('cintura')
        cadera = data.get('cadera')
        cuello = data.get('cuello')
        altura = data.get('altura')
        genero = data.get('genero', '').strip().lower()

        # Mostrar valores recibidos para depuración
        print(f"Datos recibidos: cintura={cintura}, cadera={cadera}, cuello={cuello}, altura={altura}, genero={genero}")

        # Validación de parámetros obligatorios
        if any(val is None for val in [cintura, cuello, altura, genero]):
            return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

        if genero not in ['h', 'm']:
            return jsonify({'error': "El valor de 'genero' debe ser 'h' o 'm'"}), 400

        # Para hombres, la cadera no es requerida
        if genero == 'm' and (cadera is None or cadera <= 0):
            return jsonify({'error': 'El valor de cadera es obligatorio y debe ser positivo para mujeres'}), 400

        # Validación de valores positivos
        if any(val <= 0 for val in [cintura, cuello, altura]) or (genero == 'm' and cadera <= 0):
            return jsonify({'error': 'Todos los valores deben ser positivos'}), 400

        # Calcular porcentaje de grasa
        resultado = calcular_porcentaje_grasa(cintura, cadera, cuello, altura, genero)
        resultado_formateado = f'{resultado:.2f}'
        return jsonify({"porcentaje_grasa": resultado_formateado})

    except ValueError as e:
        # Capturar errores de valor y devolver un mensaje de error
        return jsonify({"error": str(e)}), 400


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
        return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

    try:
        resultado = calcular_agua_total(peso, altura, edad, genero)
        return jsonify({"agua_total": resultado})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/calcular_peso_saludable', methods=['POST'])
def calcular_peso_saludable_endpoint():
    try:
        data = request.get_json()
        altura = data.get('altura')

        # Validación de parámetro obligatorio
        if altura is None:
            return jsonify({'error': 'Faltan parámetros obligatorios'}), 400

        resultado_min, resultado_max = calcular_peso_saludable(altura)
        resultado_formateado = {
            "peso_min": f"{resultado_min:.2f}",
            "peso_max": f"{resultado_max:.2f}"
        }
        return jsonify({"peso_saludable": resultado_formateado}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except TypeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/calcular_sobrepeso', methods=['POST'])
def calcular_sobrepeso_endpoint():
    try:
        # Obtener datos de la solicitud
        data = request.get_json()
        peso = data.get('peso')
        altura = data.get('altura')

        # Validación de parámetros obligatorios
        if peso is None or altura is None:
            return jsonify({'error': 'Faltan parámetros obligatorios: peso y altura son requeridos'}), 400

        # Calcular sobrepeso
        resultado = calcular_sobrepeso(peso, altura)
        resultado_formateado = f'{resultado:.2f}'

        # Devolver el resultado formateado en JSON
        return jsonify({"sobrepeso": resultado_formateado}), 200

    except ValueError as e:
        # Capturar errores de valor y devolver un mensaje de error
        return jsonify({"error": str(e)}), 400


@app.route('/calcular_rcc', methods=['POST'])
def calcular_rcc_endpoint():
    """
    Endpoint para calcular la Relación Cintura-Cadera (RCC).

    Args (JSON):
        cintura (float): Medida de la cintura en centímetros.
        cadera (float): Medida de la cadera en centímetros.

    Returns:
        JSON: Relación Cintura-Cadera calculada con dos decimales o un mensaje de error.
    """
    # Obtener datos de la solicitud
    data = request.get_json()
    cintura = data.get('cintura')
    cadera = data.get('cadera')

    # Validación de parámetros obligatorios y valores positivos
    if cintura is None or cadera is None:
        return jsonify({'error': 'Faltan parámetros obligatorios: cintura y cadera son requeridos'}), 400
    if cintura <= 0 or cadera <= 0:
        return jsonify({'error': 'Los valores de cintura y cadera deben ser positivos'}), 400

    try:
        # Calcular RCC
        resultado = calcular_rcc(cintura, cadera)
        resultado_formateado = f'{resultado:.2f}'

        # Devolver el resultado formateado en JSON
        return jsonify({"rcc": resultado_formateado}), 200

    except ValueError as e:
        # Capturar errores de valor y devolver un mensaje de error
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
