from calculos import (
    calcular_agua_total,
    calcular_imc,
    calcular_peso_saludable,
    calcular_porcentaje_grasa,
    calcular_rcc,
    calcular_sobrepeso,
    calcular_tmb,
)
from flask import jsonify, request

from .model import Sexo


def configure_routes(app):
    @app.route("/calcular_porcentaje_grasa", methods=["POST"])
    def calcular_grasa_endpoint():
        try:
            # Obtener datos de la solicitud
            data = request.get_json()
            cintura = data.get("cintura")
            cadera = data.get("cadera", None)
            cuello = data.get("cuello")
            altura = data.get("altura")
            genero = data.get("genero")

            # Validación de los parámetros
            if genero not in [Sexo.HOMBRE.value, Sexo.MUJER.value]:
                return (
                    jsonify({"error": "El valor de 'genero' debe ser 'h' o 'm'."}),
                    400,
                )

            resultado = calcular_porcentaje_grasa(
                cintura, cadera, cuello, altura, Sexo(genero)
            )
            return jsonify({"porcentaje_grasa": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_sobrepeso", methods=["POST"])
    def calcular_sobrepeso_endpoint():
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")

            if None in (peso, altura):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_sobrepeso(peso, altura)
            return jsonify({"sobrepeso": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_rcc", methods=["POST"])
    def calcular_rcc_endpoint():
        try:
            data = request.get_json()
            cintura = data.get("cintura")
            cadera = data.get("cadera")

            if None in (cintura, cadera):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_rcc(cintura, cadera)
            return jsonify({"rcc": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_tmb", methods=["POST"])
    def calcular_tmb_endpoint():
        data = request.get_json()
        peso = data["peso"]
        altura = data["altura"]
        edad = data["edad"]
        genero = data["genero"]

        if None in (peso, altura, edad, genero):
            return jsonify({"error": "Faltan parámetros obligatorios"}), 400

        try:
            resultado = calcular_tmb(peso, altura, edad, genero)
            return jsonify({"tmb": resultado})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_imc", methods=["POST"])
    def calcular_imc_endpoint():
        data = request.get_json()
        peso = data["peso"]
        altura = data["altura"]

        if None in (peso, altura):
            return (
                jsonify({"error": "Faltan parámetros obligatorios separados por coma"}),
                400,
            )

        try:
            resultado = calcular_imc(peso, altura)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"imc": resultado})

    @app.route("/calcular_agua_total", methods=["POST"])
    def calcular_agua_total_endpoint():
        data = request.get_json()
        peso = data["peso"]
        altura = data["altura"]
        edad = data["edad"]
        genero = data["genero"]

        if None in (peso, altura, edad, genero):
            return jsonify({"error": "Faltan parámetros obligatorios"}), 400

        try:
            resultado = calcular_agua_total(peso, altura, edad, genero)
            return jsonify({"agua_total": resultado})
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_peso_saludable", methods=["POST"])
    def calcular_peso_saludable_endpoint():
        try:
            data = request.get_json()
            altura = data.get("altura")

            # Validación de parámetro obligatorio
            if altura is None:
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado_min, resultado_max = calcular_peso_saludable(altura)
            resultado_formateado = {
                "peso_min": f"{resultado_min:.2f}",
                "peso_max": f"{resultado_max:.2f}",
            }
            return jsonify({"peso_saludable": resultado_formateado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except TypeError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/calcular_sobrepeso", methods=["POST"])
    def calcular_sobrepeso_endpoint():
        try:
            # Obtener datos de la solicitud
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")

            # Validación de parámetros obligatorios
            if peso is None or altura is None:
                return (
                    jsonify(
                        {
                            "error": "Faltan parámetros obligatorios: peso y altura son requeridos"
                        }
                    ),
                    400,
                )

            # Calcular sobrepeso
            resultado = calcular_sobrepeso(peso, altura)
            resultado_formateado = f"{resultado:.2f}"

            # Devolver el resultado formateado en JSON
            return jsonify({"sobrepeso": resultado_formateado}), 200

        except ValueError as e:
            # Capturar errores de valor y devolver un mensaje de error
            return jsonify({"error": str(e)}), 400
