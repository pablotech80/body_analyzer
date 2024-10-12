import flask, math
from typing import Literal, Union

app = flask.Flask(__name__)


# Funciones Lógicas
def calcular_porcentaje_grasa(
    cintura: Union[int, float],
    cadera: Union[float, None],
    cuello: Union[int, float],
    altura: Union[int, float],
    genero: Literal['h', 'm']
) -> float:
    """
    Calcula el porcentaje de grasa corporal utilizando la fórmula de la Marina de los EE.UU.
    Args:
    :param cintura: Circunferencia de la cintura en cm. (float)
    :param cadera:  Circunferencia de la cadera en cm, solo para mujeres.(float)
    :param cuello:  Circunferencia del cuello en cm. (float)
    :param altura:  Altura en cm.(float, int)
    :param genero: Género de la persona, 'h' para hombre y 'm' para mujer.
    :return: Porcentaje de grasa corporal redondeado a dos decimales.
    """

    if genero == 'h':
        porcentaje_grasa = 495 / (
                1.0324 - 0.19077 * math.log10(cintura - cuello) + 0.15456 * math.log10(altura)) - 450

    elif genero == 'm':
        if cadera is None:
            raise ValueError("Para mujeres, la cadera debe ser especificada.")
        porcentaje_grasa = 495 / (
                1.29579 - 0.35004 * math.log10(cintura + cadera - cuello) + 0.22100 * math.log10(altura)) - 450
        return round(porcentaje_grasa, 2)
    else:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")
    return round(porcentaje_grasa, 2)


def calcular_tmb(
        peso: Union[int, float],
        altura: Union[int, float],
        edad: Union[int],
        genero: Literal['h', 'm']) -> float:
    """Calcula la tasa Metabólica Basal(TMB) usando la fórmula de Harris-Benedict.

    Args:
        peso: Peso en kg.(float)
        altura: Altura en cm.(float, int)
        edad: Edad del usuario en años (int)
        genero: (Literal) 'h' para hombre y 'm' para mujer.

    Returns: float: TMB calculada.
        """
    # Validaciones de entrada

    if peso <= 0:
        raise ValueError("El peso debe ser un valor positivo.")
    if altura <= 0:
        raise ValueError("La altura debe ser un valor positivo.")
    if edad <= 0:
        raise ValueError("La edad debe ser un valor positivo.")

    if genero == 'h':
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    elif genero == 'm':
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    else:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")
    return round(tmb, 2)

def calcular_imc(
        peso: Union[int, float],
        altura: Union[int, float]) -> float:

    """Calcula el Índice de Masa Corporal (IMC).
    Args:
        peso: Peso en kg.(float) Peso del usuario en kg.
        altura: Altura en cm.(float, int) Altura del usuario en cm.
    Returns: float: IMC calculada.
    """
    # Validaciones de entrada
    if peso <= 0:
        raise ValueError("El peso debe ser un valor positivo.")
    if altura <= 0:
        raise ValueError("La altura debe ser un valor positivo.")
    altura_m = altura / 100     # Esta variable convierte la altura de metros a cm.
    imc = peso / (altura_m ** 2)
    return round(imc, 2)

