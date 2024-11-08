from .calculos import *
from .interpretaciones import *
from .model import Sexo


def validar_parametro(nombre, valor, tipos, positivo=True):
    """
    Valida que el parámetro `valor` sea de uno de los `tipos` indicados y, si se requiere,
    que sea positivo.
    """
    if not isinstance(valor, tipos) or (positivo and valor <= 0):
        tipo_str = ", ".join([t.__name__ for t in tipos])
        raise ValueError(f"'{nombre}' debe ser un {tipo_str} positivo.")


def calcular_resultados(peso, altura, edad, genero_enum, cintura, cuello, cadera):
    """
    Realiza cálculos principales como TMB, IMC, porcentaje de grasa, etc., y devuelve un diccionario
    con los resultados.
    """
    return {
        "tmb": calcular_tmb(peso, altura, edad, genero_enum),
        "imc": calcular_imc(peso, altura),
        "porcentaje_grasa": calcular_porcentaje_grasa(
            cintura, cuello, altura, genero_enum, cadera
        ),
        "peso_grasa_corporal": calcular_peso_grasa_corporal(
            peso,
            calcular_porcentaje_grasa(cintura, cuello, altura, genero_enum, cadera),
        ),
        "masa_muscular": peso
        - calcular_peso_grasa_corporal(
            peso,
            calcular_porcentaje_grasa(cintura, cuello, altura, genero_enum, cadera),
        ),
        "ffmi": calcular_masa_muscular(
            peso,
            calcular_porcentaje_grasa(cintura, cuello, altura, genero_enum, cadera),
        ),
        "rcc": calcular_rcc(cintura, cadera) if genero_enum == Sexo.MUJER else "N/A",
        "ratio_cintura_altura": cintura / altura,
    }


def calcular_interpretaciones(resultados, genero_enum):
    """
    Realiza las interpretaciones de los resultados y devuelve un diccionario con las interpretaciones.
    """
    return {
        "ffmi": interpretar_ffmi(resultados["ffmi"], genero_enum),
        "imc": interpretar_imc(resultados["imc"], resultados["ffmi"], genero_enum),
        "porcentaje_grasa": interpretar_porcentaje_grasa(
            resultados["porcentaje_grasa"], genero_enum
        ),
        "rcc": (
            interpretar_rcc(resultados["rcc"], genero_enum)
            if genero_enum == Sexo.MUJER
            else "N/A"
        ),
        "ratio_cintura_altura": interpretar_ratio_cintura_altura(
            resultados["ratio_cintura_altura"]
        ),
    }


def informe_completo(data):
    try:
        # Extracción y validación de datos simplificando con un bucle
        campos_obligatorios = ["peso", "altura", "edad", "genero", "cuello", "cintura"]
        for campo in campos_obligatorios:
            if data.get(campo) is None:
                raise ValueError(f"Falta el parámetro obligatorio: {campo}")
        peso, altura, edad, genero, cuello, cintura = [
            data.get(c) for c in campos_obligatorios
        ]
        cadera = data.get("cadera") if genero == "m" else None

        # Validación de valores y tipos
        validar_parametro("peso", peso, (int, float))
        validar_parametro("altura", altura, (int, float))
        validar_parametro("edad", edad, (int,))
        validar_parametro("cuello", cuello, (int, float))
        validar_parametro("cintura", cintura, (int, float))
        if genero == "m":
            validar_parametro("cadera", cadera, (int, float))
        genero_enum = Sexo.HOMBRE if genero == "h" else Sexo.MUJER

        # Realización de cálculos e interpretaciones
        resultados = calcular_resultados(
            peso, altura, edad, genero_enum, cintura, cuello, cadera
        )
        interpretaciones = calcular_interpretaciones(resultados, genero_enum)

        return {"resultados": resultados, "interpretaciones": interpretaciones}

    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Error interno del servidor: {str(e)}"}
