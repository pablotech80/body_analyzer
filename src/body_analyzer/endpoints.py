from flask import jsonify, request

from .calculos import *
from .constantes import *
from .model import Sexo


def configure_routes(app):
    """
    Configura las rutas de la aplicación Flask.

    :param app: Objeto de la aplicación Flask.
    :return: None
    """

    @app.route("/calcular_porcentaje_grasa", methods=["POST"])
    def calcular_grasa_endpoint():
        """
        Calcula el porcentaje de grasa corporal basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - cintura: Circunferencia de cintura (obligatorio)
        - cadera: Circunferencia de cadera (opcional)
        - cuello: Circunferencia de cuello (obligatorio)
        - altura: Altura de la persona (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con el porcentaje de grasa o un mensaje de error.
        """
        try:
            data = request.get_json()
            cintura = data.get("cintura")
            cadera = data.get("cadera")
            cuello = data.get("cuello")
            altura = data.get("altura")
            genero = data.get("genero")

            if None in (cintura, cuello, altura, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400
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
        """
        Calcula el sobrepeso basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - peso: Peso de la persona (obligatorio)
        - altura: Altura de la persona (obligatorio)

        :return: Un JSON con el sobrepeso calculado o un mensaje de error.
        """
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")

            if None in (peso, altura):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_sobrepeso(peso, altura)
            return jsonify({"sobrepeso": f"{resultado:.2f}"}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_rcc", methods=["POST"])
    def calcular_rcc_endpoint():
        """
        Calcula el ratio cintura-cadera (RCC) basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - cintura: Circunferencia de cintura (obligatorio)
        - cadera: Circunferencia de cadera (obligatorio)

        :return: Un JSON con el RCC calculado o un mensaje de error.
        """
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
        """
        Calcula la tasa metabólica basal (TMB) basada en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - peso: Peso de la persona (obligatorio)
        - altura: Altura de la persona (obligatorio)
        - edad: Edad de la persona (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la TMB calculada o un mensaje de error.
        """
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")
            edad = data.get("edad")
            genero = data.get("genero")

            if None in (peso, altura, edad, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_tmb(peso, altura, edad, genero)
            return jsonify({"tmb": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_imc", methods=["POST"])
    def calcular_imc_endpoint():
        """
        Calcula el índice de masa corporal (IMC) basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - peso: Peso de la persona (obligatorio)
        - altura: Altura de la persona (obligatorio)

        :return: Un JSON con el IMC calculado o un mensaje de error.
        """
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")

            if None in (peso, altura):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_imc(peso, altura)
            return jsonify({"imc": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_agua_total", methods=["POST"])
    def calcular_agua_total_endpoint():
        """
        Calcula el total de agua corporal basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - peso: Peso de la persona (obligatorio)
        - altura: Altura de la persona (obligatorio)
        - edad: Edad de la persona (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la cantidad de agua total o un mensaje de error.
        """
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")
            edad = data.get("edad")
            genero = data.get("genero")

            if None in (peso, altura, edad, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            resultado = calcular_agua_total(peso, altura, edad, genero)
            return jsonify({"agua_total": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/calcular_peso_saludable", methods=["POST"])
    def calcular_peso_saludable_endpoint():
        """
        Calcula el rango de peso saludable basado en la altura recibida.

        Parámetros de la solicitud JSON:
        - altura: Altura de la persona (obligatorio)

        :return: Un JSON con el rango de peso saludable o un mensaje de error.
        """
        try:
            data = request.get_json()
            altura = data.get("altura")

            if altura is None:
                return (
                    jsonify({"error": "Falta el parámetro obligatorio 'altura'"}),
                    400,
                )

            resultado_min, resultado_max = calcular_peso_saludable(altura)
            return (
                jsonify(
                    {
                        "peso_min": f"{resultado_min:.2f}",
                        "peso_max": f"{resultado_max:.2f}",
                    }
                ),
                200,
            )

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/interpretar_imc", methods=["POST"])
    def interpretar_imc_endpoint():
        """
        Interpreta el IMC recibido junto con el FFMI y el género.

        Parámetros de la solicitud JSON:
        - imc: Índice de masa corporal (obligatorio)
        - ffmi: Índice de masa libre de grasa (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la interpretación del IMC o un mensaje de error.
        """
        try:
            data = request.get_json()
            imc = data.get("imc")
            ffmi = data.get("ffmi")
            genero = data.get("genero")

            if None in (imc, ffmi, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400
            if genero not in [Sexo.HOMBRE, Sexo.MUJER]:
                return jsonify({"error": "Género no válido"}), 400

            if imc > 25 and ffmi > 16:
                resultado = "El IMC es alto, pero puede estar influenciado por una alta masa muscular."
            elif imc < 18.5:
                resultado = "El IMC es bajo, se recomienda consultar con un profesional de salud."
            else:
                resultado = "El IMC está dentro del rango normal."

            return jsonify({"interpretacion_imc": resultado})

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/interpretar_porcentaje_grasa", methods=["POST"])
    def interpretar_porcentaje_grasa_endpoint():
        """
        Interpreta el porcentaje de grasa recibido junto con el género.

        Parámetros de la solicitud JSON:
        - porcentaje_grasa: Porcentaje de grasa corporal (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la interpretación del porcentaje de grasa o un mensaje de error.
        """
        try:
            data = request.get_json()
            porcentaje_grasa = data.get("porcentaje_grasa")
            genero = data.get("genero")

            if None in (porcentaje_grasa, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400
            if genero not in [Sexo.HOMBRE, Sexo.MUJER]:
                return jsonify({"error": "Género no válido"}), 400

            if genero == Sexo.HOMBRE:
                if porcentaje_grasa > GRASA_ALTA_HOMBRES:
                    resultado = "Alto"
                elif porcentaje_grasa < GRASA_BAJA_HOMBRES:
                    resultado = "Bajo"
                else:
                    resultado = "Normal"
            else:  # Sexo.MUJER
                if porcentaje_grasa > GRASA_ALTA_MUJERES:
                    resultado = "Alto"
                elif porcentaje_grasa < GRASA_BAJA_MUJERES:
                    resultado = "Bajo"
                else:
                    resultado = "Normal"

            return jsonify({"interpretacion_grasa": resultado})

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/interpretar_ffmi", methods=["POST"])
    def interpretar_ffmi_endpoint():
        """
        Interpreta el FFMI recibido junto con el género.

        Parámetros de la solicitud JSON:
        - ffmi: Índice de masa libre de grasa (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la interpretación del FFMI o un mensaje de error.
        """
        try:
            data = request.get_json()
            ffmi = data.get("ffmi")
            genero = data.get("genero")

            if None in (ffmi, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400
            if genero not in [Sexo.HOMBRE, Sexo.MUJER]:
                return jsonify({"error": "Género no válido"}), 400

            umbrales = (
                FFMI_UMBRAL_HOMBRES if genero == Sexo.HOMBRE else FFMI_UMBRAL_MUJERES
            )

            if ffmi < umbrales[0]:
                resultado = "Lejos del máximo potencial (pobre forma física)."
            elif umbrales[0] <= ffmi < umbrales[1]:
                resultado = "Cercano a la normalidad."
            elif umbrales[1] <= ffmi < umbrales[2]:
                resultado = "Normal."
            elif umbrales[2] <= ffmi < umbrales[3]:
                resultado = "Superior a la normalidad (buena forma física)."
            elif umbrales[3] <= ffmi < umbrales[4]:
                resultado = "Fuerte (muy buena forma física)."
            elif umbrales[4] <= ffmi < umbrales[5]:
                resultado = (
                    "Muy fuerte (excelente forma física). Cerca del máximo potencial."
                )
            elif umbrales[5] <= ffmi < umbrales[6]:
                resultado = "Muy cerca del máximo potencial."
            else:
                resultado = "Potencial máximo natural alcanzado. Muy muy pocos llegan naturales."

            return jsonify({"interpretacion_ffmi": resultado})

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/interpretar_rcc", methods=["POST"])
    def interpretar_rcc_endpoint():
        """
        Interpreta el ratio cintura-cadera (RCC) recibido junto con el género.

        Parámetros de la solicitud JSON:
        - rcc: Ratio cintura-cadera (obligatorio)
        - genero: Género de la persona ('h' para hombre, 'm' para mujer) (obligatorio)

        :return: Un JSON con la interpretación del RCC o un mensaje de error.
        """
        try:
            data = request.get_json()
            rcc = data.get("rcc")
            genero = data.get("genero")

            if None in (rcc, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400
            if genero not in [Sexo.HOMBRE, Sexo.MUJER]:
                return jsonify({"error": "Género no válido"}), 400

            if genero == Sexo.HOMBRE:
                if rcc > RCC_ALTO_HOMBRES:
                    resultado = "Alto riesgo."
                elif RCC_MODERADO_HOMBRES < rcc <= RCC_ALTO_HOMBRES:
                    resultado = "Moderado riesgo."
                else:
                    resultado = "Bajo riesgo."
            else:  # Sexo.MUJER
                if rcc > RCC_ALTO_MUJERES:
                    resultado = "Alto riesgo."
                elif RCC_MODERADO_MUJERES < rcc <= RCC_ALTO_MUJERES:
                    resultado = "Moderado riesgo."
                else:
                    resultado = "Bajo riesgo."

            return jsonify({"interpretacion_rcc": resultado})

        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/interpretar_ratio_cintura_altura", methods=["POST"])
    def interpretar_ratio_cintura_altura_endpoint():
        """
        Interpreta el ratio cintura-altura recibidos.

        Parámetros de la solicitud JSON:
        - ratio: Ratio cintura-altura (obligatorio)

        :return: Un JSON con la interpretación del ratio cintura-altura o un mensaje de error.
        """
        try:
            data = request.get_json()
            ratio = data.get("ratio")

            if ratio <= 0:
                return (
                    jsonify(
                        {"error": "El valor del 'ratio' debe ser un número positivo"}
                    ),
                    400,
                )

            if ratio >= RATIO_ALTO_RIESGO:
                resultado = "Alto riesgo."
            elif RATIO_MODERADO_RIESGO <= ratio < RATIO_ALTO_RIESGO:
                resultado = "Moderado riesgo."
            else:
                resultado = "Bajo riesgo."

            return jsonify({"interpretacion_ratio_cintura_altura": resultado})

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
