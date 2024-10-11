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
