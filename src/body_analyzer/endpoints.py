from flask import json, jsonify, request, Response, Blueprint

from src.body_analyzer.interpretaciones import *


from src.body_analyzer.model import Sexo
from .analisis_completo import validar_parametro

from .calculos import *
from .constantes import *


bp = Blueprint("body_analyzer", __name__)


def configure_routes(app):
    app.register_blueprint(bp)
    print("Configuring routes")
    """
    Configura las rutas de la aplicación Flask.

    :param app: Objeto de la aplicación Flask.
    :return: None
    """

    @app.route("/")
    def index():
        return "Welcome to the BIO*ANALYZE API!"

    @app.route("/calcular_porcentaje_grasa", methods=["POST"])
    def calcular_porcentaje_grasa_endpoint():
        try:
            data = request.get_json()
            cintura = data.get("cintura")
            cuello = data.get("cuello")
            altura = data.get("altura")
            genero = data.get("genero")
            cadera = data.get("cadera")

            # Verificar los parámetros requeridos para hombres y mujeres
            if None in (cintura, cuello, altura, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            # Verificar que el género sea válido
            if genero not in ["h", "m"]:
                return (
                    jsonify({"error": "El valor de 'genero' debe ser 'h' o 'm'."}),
                    400,
                )

            # Verificar el valor de cadera si el género es mujer
            if genero == "m" and cadera is None:
                return (
                    jsonify(
                        {"error": "Para mujeres, la cadera debe ser especificada."}
                    ),
                    400,
                )

            # Convertir genero a Enum Sexo
            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

            # Calcular el porcentaje de grasa
            porcentaje_grasa = calcular_porcentaje_grasa(
                cintura, cuello, altura, genero_enum, cadera
            )

            return jsonify({"porcentaje_grasa": round(porcentaje_grasa, 2)}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @app.route("/calcular_peso_grasa_corporal", methods=["POST"])
    def calcular_peso_grasa_corporal_endpoint():
        """
        Calcula el peso de la grasa corporal basado en los parámetros recibidos.

        Parámetros de la solicitud JSON:
        - peso: Peso total de la persona en kilogramos (obligatorio).
        - porcentaje_grasa: Porcentaje de grasa corporal (entre 0 y 100) (obligatorio).

        :return: Un JSON con el peso de la grasa corporal en kilogramos o un mensaje de error.
        """
        try:
            # Obtener los datos del cuerpo de la solicitud
            data = request.get_json()

            # Comprobación de existencia de parámetros
            if "peso" not in data or "porcentaje_grasa" not in data:
                return (
                    jsonify(
                        {
                            "error": "Faltan parámetros obligatorios: 'peso' y 'porcentaje_grasa'."
                        }
                    ),
                    400,
                )

            peso = data.get("peso")
            porcentaje_grasa = data.get("porcentaje_grasa")

            # Validación de tipos de datos y valores
            if not isinstance(peso, float):
                return (
                    jsonify(
                        {"error": "El valor de 'peso' debe ser un número positivo."}
                    ),
                    400,
                )
            if not isinstance(porcentaje_grasa, float):
                return (
                    jsonify(
                        {
                            "error": "El valor de 'porcentaje_grasa' debe ser un número entre 0 y 100."
                        }
                    ),
                    400,
                )

            # Validación de rango de valores
            if peso <= 0:
                return jsonify({"error": "El peso debe ser un número positivo."}), 400
            if not (0 <= porcentaje_grasa <= 100):
                return (
                    jsonify(
                        {"error": "El porcentaje de grasa debe estar entre 0 y 100."}
                    ),
                    400,
                )

            # Calcular el peso de la grasa corporal
            resultado = calcular_peso_grasa_corporal(peso, porcentaje_grasa)

            # Devolver el resultado
            return jsonify({"peso_grasa_corporal": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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

            # Validación de parámetros obligatorios
            peso = data.get("peso")
            altura = data.get("altura")

            if None in (peso, altura):
                return (
                    jsonify(
                        {
                            "error": "Faltan parámetros obligatorios: peso y altura son requeridos."
                        }
                    ),
                    400,
                )

            # Validación adicional de tipos de datos
            if not isinstance(peso, (int, float)) or not isinstance(
                altura, (int, float)
            ):
                return (
                    jsonify(
                        {
                            "error": "Los parámetros 'peso' y 'altura' deben ser numéricos."
                        }
                    ),
                    400,
                )

            if peso <= 0 or altura <= 0:
                return (
                    jsonify(
                        {
                            "error": "Los valores de 'peso' y 'altura' deben ser mayores que 0."
                        }
                    ),
                    400,
                )

            # Calcular sobrepeso
            resultado = calcular_sobrepeso(peso, altura)

            return jsonify({"sobrepeso": f"{resultado:.2f}"}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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
        Endpoint para calcular la Tasa Metabólica Basal (TMB) usando la fórmula de Harris-Benedict.

        Parámetros de la solicitud JSON:
        - peso: Peso en kg (obligatorio, float)
        - altura: Altura en cm (obligatorio, float)
        - edad: Edad del usuario en años (obligatorio, int)
        - genero: Género del usuario ('h' para hombre, 'm' para mujer) (obligatorio, str)

        :return: Un JSON con el TMB calculado o un mensaje de error.
        """
        try:
            # Obtener los datos del cuerpo de la solicitud
            data = request.get_json()

            # Validación de que la solicitud contiene datos válidos
            if not data:
                return (
                    jsonify(
                        {"error": "El cuerpo de la solicitud debe ser un JSON válido."}
                    ),
                    400,
                )

            # Extracción de los parámetros
            peso = data.get("peso")
            altura = data.get("altura")
            edad = data.get("edad")
            genero = data.get("genero")

            # Validación básica de los parámetros
            if None in (peso, altura, edad, genero):
                return (
                    jsonify(
                        {
                            "error": "Faltan parámetros obligatorios: peso, altura, edad o genero"
                        }
                    ),
                    400,
                )

            # Validación de los tipos de datos
            try:
                peso = float(peso)
                altura = float(altura)
                edad = int(edad)
            except ValueError:
                return (
                    jsonify(
                        {
                            "error": "Peso y altura deben ser numéricos, y la edad debe ser un entero."
                        }
                    ),
                    400,
                )

            # Validación de que los valores sean razonables
            if peso <= 0 or altura <= 0 or edad <= 0:
                return (
                    jsonify(
                        {"error": "Peso, altura y edad deben ser mayores que cero."}
                    ),
                    400,
                )

            # Validación del género
            if genero not in ["h", "m"]:
                return (
                    jsonify({"error": "El valor de 'genero' debe ser 'h' o 'm'."}),
                    400,
                )

            # Calcular TMB
            if genero == "h":
                tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
            elif genero == "m":
                tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)

            # Asegurarse de que el resultado de TMB no es None o vacío y que es razonable
            if tmb is None or tmb <= 0:
                return (
                    jsonify(
                        {"error": "Error en el cálculo de TMB o resultado inválido"}
                    ),
                    500,
                )

            # Devolver el resultado de TMB
            return jsonify({"tmb": round(tmb, 2)}), 200

        except ValueError as e:
            return jsonify({"error": f"Error en el valor de entrada: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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

            # Verificar si todos los parámetros obligatorios están presentes
            if None in (peso, altura, edad, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            # Validar genero ('h' o 'm')
            if genero not in ["h", "m"]:
                return (
                    jsonify({"error": "El valor de 'genero' debe ser 'h' o 'm'."}),
                    400,
                )

            # Convertir genero a Enum Sexo
            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

            # Llamar a la función de cálculo
            resultado = calcular_agua_total(peso, altura, edad, genero_enum)
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
        try:
            # Obtener los datos del cuerpo de la solicitud
            data = request.get_json()
            imc = data.get("imc")
            ffmi = data.get("ffmi")
            genero = data.get("genero")

            # Validación de que los parámetros no sean nulos
            if None in (imc, ffmi, genero):
                return (
                    jsonify(
                        {"error": "Faltan parámetros obligatorios: imc, ffmi o genero"}
                    ),
                    400,
                )

            # Validación del género: convertir a la enumeración Sexo
            if genero == "h":
                Sexo.HOMBRE
            elif genero == "m":
                Sexo.MUJER
            else:
                return jsonify({"error": "Género no válido"}), 400

            # Interpretar IMC
            if imc > 25 and ffmi > 16:
                resultado = "El IMC es alto, pero puede estar influenciado por una alta masa muscular."
            elif imc < 18.5:
                resultado = "El IMC es bajo, se recomienda consultar con un profesional de salud."
            else:
                resultado = "El IMC está dentro del rango normal."

            # Devolver el resultado de la interpretación
            return jsonify({"interpretacion_imc": resultado}), 200

        except ValueError as e:
            return jsonify({"error": f"Error en el valor de entrada: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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

            # Validación de parámetros obligatorios
            if None in (porcentaje_grasa, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            # Validación del género
            if genero not in ["h", "m"]:
                return jsonify({"error": "Género no válido"}), 400

            # Convertir el género a la clase Enum Sexo
            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

            # Interpreta el porcentaje de grasa basado en el género
            if genero_enum == Sexo.HOMBRE:
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

            return jsonify({"interpretacion_grasa": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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

            # Validación de parámetros obligatorios
            if None in (ffmi, genero):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            # Validación de tipo de dato
            if not isinstance(ffmi, (int, float)):
                return jsonify({"error": "El valor de 'ffmi' debe ser numérico"}), 400

            # Validación del género
            if genero not in ["h", "m"]:
                return (
                    jsonify(
                        {
                            "error": "El valor de 'genero' debe ser 'h' para hombre o 'm' para mujer"
                        }
                    ),
                    400,
                )

            # Convertir genero a Enum Sexo
            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

            # Definir los umbrales según el género
            umbrales = (
                FFMI_UMBRAL_HOMBRES
                if genero_enum == Sexo.HOMBRE
                else FFMI_UMBRAL_MUJERES
            )

            # Interpretación del FFMI
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

            return jsonify({"interpretacion_ffmi": resultado}), 200

        except ValueError as e:
            return jsonify({"error": f"Error en el valor de entrada: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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
            # Obtener datos del cuerpo de la solicitud
            data = request.get_json()
            rcc = data.get("rcc")
            genero = data.get("genero")

            # Validación de que los parámetros no sean nulos
            if rcc is None or genero is None:
                return (
                    jsonify({"error": "Faltan parámetros obligatorios: rcc y genero"}),
                    400,
                )

            # Validación de los tipos de datos
            if not isinstance(rcc, (int, float)):
                return jsonify({"error": "El valor de 'rcc' debe ser numérico."}), 400

            # Validación del género
            if genero not in ["h", "m"]:
                return (
                    jsonify({"error": "El valor de 'genero' debe ser 'h' o 'm'."}),
                    400,
                )

            # Asignar umbrales basados en el género
            if genero == "h":
                if rcc > RCC_ALTO_HOMBRES:
                    resultado = "Alto riesgo."
                elif RCC_MODERADO_HOMBRES < rcc <= RCC_ALTO_HOMBRES:
                    resultado = "Moderado riesgo."
                else:
                    resultado = "Bajo riesgo."
            else:  # genero == 'm'
                if rcc > RCC_ALTO_MUJERES:
                    resultado = "Alto riesgo."
                elif RCC_MODERADO_MUJERES < rcc <= RCC_ALTO_MUJERES:
                    resultado = "Moderado riesgo."
                else:
                    resultado = "Bajo riesgo."

            return jsonify({"interpretacion_rcc": resultado}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

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

            # Validación de que el parámetro ratio no sea nulo y sea un valor numérico positivo
            if ratio is None:
                return jsonify({"error": "Falta el parámetro obligatorio 'ratio'"}), 400
            if not isinstance(ratio, (int, float)):
                return jsonify({"error": "El valor de 'ratio' debe ser un número"}), 400
            if ratio <= 0:
                return (
                    jsonify(
                        {"error": "El valor de 'ratio' debe ser un número positivo"}
                    ),
                    400,
                )

            # Interpretación del ratio cintura-altura
            if ratio >= RATIO_ALTO_RIESGO:
                resultado = "Alto riesgo."
            elif RATIO_MODERADO_RIESGO <= ratio < RATIO_ALTO_RIESGO:
                resultado = "Moderado riesgo."
            else:
                resultado = "Bajo riesgo."

            return jsonify({"interpretacion_ratio_cintura_altura": resultado}), 200

        except ValueError as e:
            return jsonify({"error": f"Error de valor: {str(e)}"}), 400
        except TypeError as e:
            return jsonify({"error": f"Error de tipo: {str(e)}"}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @app.route("/calorias_diarias", methods=["POST"])
    def calorias_diarias_endpoint():
        """
        Endpoint para calcular las calorías diarias basadas en TMB y objetivo nutricional.
        """
        try:
            data = request.get_json()

            # Validación de parámetros necesarios
            peso = data.get("peso")
            altura = data.get("altura")
            edad = data.get("edad")
            genero = data.get("genero")
            objetivo = data.get("objetivo")

            # Validación de valores
            if None in (peso, altura, edad, genero, objetivo):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER
            try:
                objetivo_enum = ObjetivoNutricional(objetivo)
            except ValueError:
                return (
                    jsonify(
                        {
                            "error": "El objetivo debe ser 'mantener peso', 'perder grasa' o 'ganar masa muscular'"
                        }
                    ),
                    400,
                )

            # Calcular TMB y luego calorías diarias
            tmb = calcular_tmb(peso, altura, edad, genero_enum)
            calorias_diarias = round(calcular_calorias_diarias(tmb, objetivo_enum), 2)

            return jsonify({"calorias_diarias": calorias_diarias}), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @app.route("/macronutrientes", methods=["POST"])
    def macronutrientes_endpoint():
        try:
            data = request.get_json()
            calorias_diarias = data.get("calorias_diarias")
            objetivo = data.get("objetivo")

            # Validaciones básicas
            if calorias_diarias is None or objetivo is None:
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            objetivo_enum = ObjetivoNutricional(objetivo.strip().lower())

            # Cálculo de macronutrientes
            proteinas, carbohidratos, grasas = calcular_macronutrientes(
                calorias_diarias, objetivo_enum
            )

            return (
                jsonify(
                    {
                        "macronutrientes": {
                            "proteinas": proteinas,
                            "carbohidratos": carbohidratos,
                            "grasas": grasas,
                        }
                    }
                ),
                200,
            )

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500

    @app.route("/informe_completo", methods=["POST"])
    def informe_completo_endpoint():
        try:
            data = request.get_json()
            peso = data.get("peso")
            altura = data.get("altura")
            edad = data.get("edad")
            genero = data.get("genero")
            cuello = data.get("cuello")
            cintura = data.get("cintura")
            cadera = data.get("cadera")
            objetivo = data.get("objetivo")

            # Validaciones
            if None in (peso, altura, edad, genero, cuello, cintura, objetivo):
                return jsonify({"error": "Faltan parámetros obligatorios"}), 400

            genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER
            objetivo_enum = ObjetivoNutricional(objetivo.strip().lower())

            # Realizar cálculos principales
            porcentaje_grasa = calcular_porcentaje_grasa(
                cintura, cuello, altura, genero_enum, cadera
            )
            tmb = calcular_tmb(peso, altura, edad, genero_enum)
            imc = calcular_imc(peso, altura)
            masa_muscular = peso - (peso * (porcentaje_grasa / 100))
            agua_total = calcular_agua_total(peso, altura, edad, genero_enum)
            ffmi = calcular_ffmi(masa_muscular, altura)
            peso_saludable_min, peso_saludable_max = calcular_peso_saludable(altura)
            sobrepeso = calcular_sobrepeso(peso, altura)
            rcc = calcular_rcc(cintura, cadera) if genero_enum == Sexo.MUJER else "N/A"
            ratio_cintura_altura = calcular_ratio_cintura_altura(cintura, altura)

            # Calorías diarias y macronutrientes
            calorias_diarias = calcular_calorias_diarias(tmb, objetivo_enum)
            proteinas, carbohidratos, grasas = calcular_macronutrientes(
                calorias_diarias, objetivo_enum
            )

            # Interpretaciones
            interpretacion_imc = interpretar_imc(imc, ffmi, genero_enum)
            interpretacion_grasa = interpretar_porcentaje_grasa(
                porcentaje_grasa, genero_enum
            )
            interpretacion_ffmi = interpretar_ffmi(ffmi, genero_enum)
            interpretacion_rcc = (
                interpretar_rcc(rcc, genero_enum)
                if genero_enum == Sexo.MUJER
                else "N/A"
            )
            interpretacion_ratio_cintura_altura = interpretar_ratio_cintura_altura(
                ratio_cintura_altura
            )

            # Consolidación del informe
            resultados = {
                "tmb": tmb,
                "imc": imc,
                "porcentaje_grasa": porcentaje_grasa,
                "masa_muscular": masa_muscular,
                "agua_total": agua_total,
                "ffmi": ffmi,
                "peso_saludable": {
                    "min": peso_saludable_min,
                    "max": peso_saludable_max,
                },
                "sobrepeso": sobrepeso,
                "rcc": rcc,
                "ratio_cintura_altura": ratio_cintura_altura,
                "calorias_diarias": calorias_diarias,
                "macronutrientes": {
                    "proteinas": proteinas,
                    "carbohidratos": carbohidratos,
                    "grasas": grasas,
                },
            }

            interpretaciones = {
                "imc": interpretacion_imc,
                "porcentaje_grasa": interpretacion_grasa,
                "ffmi": interpretacion_ffmi,
                "rcc": interpretacion_rcc,
                "ratio_cintura_altura": interpretacion_ratio_cintura_altura,
            }

            informe = {"resultados": resultados, "interpretaciones": interpretaciones}

            return jsonify(informe), 200

        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": f"Error interno del servidor: {str(e)}"}), 500
