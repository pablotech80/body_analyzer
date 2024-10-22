from .calculos import *
from .interpretaciones import *
from .model import Sexo


def informe_completo(data):
    try:
        # Extracción de datos
        peso = data.get("peso")
        altura = data.get("altura")
        edad = data.get("edad")
        genero = data.get("genero")
        cuello = data.get("cuello")
        cintura = data.get("cintura")
        cadera = (
            data.get("cadera") if genero == "m" else None
        )  # Solo relevante para mujeres

        # Validación de parámetros obligatorios
        if None in (peso, altura, edad, genero, cuello, cintura):
            raise ValueError("Faltan parámetros obligatorios.")

        # Validación de tipos de datos
        if not isinstance(peso, (int, float)) or peso <= 0:
            raise ValueError("El peso debe ser un número positivo.")
        if not isinstance(altura, (int, float)) or altura <= 0:
            raise ValueError("La altura debe ser un número positivo.")
        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        if not isinstance(cuello, (int, float)) or cuello <= 0:
            raise ValueError("El valor de 'cuello' debe ser un número positivo.")
        if not isinstance(cintura, (int, float)) or cintura <= 0:
            raise ValueError("El valor de 'cintura' debe ser un número positivo.")
        if genero not in ["h", "m"]:
            raise ValueError(f"El valor de 'genero' debe ser 'h' o 'm': {genero}")
        if genero == "m" and (
            cadera is None or not isinstance(cadera, (int, float)) or cadera <= 0
        ):
            raise ValueError(
                "El valor de 'cadera' debe ser un número positivo para mujeres."
            )

        # Convertir genero a Enum Sexo
        genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

        # Realización de cálculos
        resultados = {
            "tmb": calcular_tmb(peso, altura, edad, genero_enum),
            "imc": calcular_imc(peso, altura),
            "porcentaje_grasa": calcular_porcentaje_grasa(
                cintura, cuello, altura, genero_enum, cadera
            ),
        }

        resultados["peso_grasa_corporal"] = calcular_peso_grasa_corporal(
            peso, resultados["porcentaje_grasa"]
        )

        resultados["masa_muscular"] = peso - resultados["peso_grasa_corporal"]
        resultados["ffmi"] = calcular_masa_muscular(
            peso, resultados["porcentaje_grasa"]
        )
        resultados["rcc"] = calcular_rcc(cintura, cadera) if genero == "m" else "N/A"
        resultados["ratio_cintura_altura"] = cintura / altura

        # Interpretaciones
        interpretaciones = {
            "ffmi": interpretar_ffmi(resultados["ffmi"], genero_enum),
            "imc": interpretar_imc(resultados["imc"], resultados["ffmi"], genero_enum),
            "porcentaje_grasa": interpretar_porcentaje_grasa(
                resultados["porcentaje_grasa"], genero_enum
            ),
            "rcc": (
                interpretar_rcc(resultados["rcc"], genero_enum)
                if genero == "m"
                else "N/A"
            ),
            "ratio_cintura_altura": interpretar_ratio_cintura_altura(
                resultados["ratio_cintura_altura"]
            ),
        }

        # Consolidar resultados e interpretaciones en un informe
        informe = {"resultados": resultados, "interpretaciones": interpretaciones}

        return informe

    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Error interno del servidor: {str(e)}"}
