import flask

app = flask.Flask(__name__)


def interpretar_imc(imc: float, ffmi: float, genero: str) -> str:
    """
    Interpreta el resultado del IMC considerando el FFMI.

    Args:
        imc (float): Índice de Masa Corporal calculado.
        ffmi (float): Índice de Masa Libre de Grasa.
        genero (str): Género del usuario ('h' para hombre, 'm' para mujer).

    Returns:
        str: Interpretación del IMC basada en los valores de FFMI y género.

    Raises:
        ValueError: Si el valor de 'genero' no es 'h' o 'm'.
    """
    # Validación del género
    if genero not in ['h', 'm']:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")

    # Interpretación basada en IMC y FFMI
    if genero == 'h':
        if imc > 25 and ffmi > 19:
            return "El IMC es alto, pero puede estar influenciado por una alta masa muscular."
    elif genero == 'm':
        if imc > 25 and ffmi > 16:
            return "El IMC es alto, pero puede estar influenciado por una alta masa muscular."

    if imc < 18.5:
        return "El IMC es bajo, se recomienda consultar con un profesional de salud."
    else:
        return "El IMC está dentro del rango normal."


# Definir constantes para los umbrales de porcentaje de grasa
GRASA_ALTA_HOMBRES = 25
GRASA_BAJA_HOMBRES = 6
GRASA_ALTA_MUJERES = 32
GRASA_BAJA_MUJERES = 16


def interpretar_porcentaje_grasa(porcentaje_grasa: float, genero: str) -> str:
    """
    Interpreta el porcentaje de grasa corporal basándose en el género y,
    proporciona una evaluación cualitativa.

    Args:
        porcentaje_grasa (float): El porcentaje de grasa corporal calculado.
        genero (str): El género del individuo ('h' para hombres, 'm' para mujeres).

    Returns:
        str: Una cadena de texto que describe el estado del porcentaje
        de grasa corporal en términos de salud.

    Raises:
        ValueError: Si el valor de 'genero' no es 'h' o 'm'.
    """
    # Validación del género
    if genero not in ['h', 'm']:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")

    # Interpretación del porcentaje de grasa
    if genero == 'h':
        if porcentaje_grasa > GRASA_ALTA_HOMBRES:
            return "Alto"
        elif porcentaje_grasa < GRASA_BAJA_HOMBRES:
            return "Bajo"
        else:
            return "Normal"
    else:  # genero == 'm'
        if porcentaje_grasa > GRASA_ALTA_MUJERES:
            return "Alto"
        elif porcentaje_grasa < GRASA_BAJA_MUJERES:
            return "Bajo"
        else:
            return "Normal"


# Constantes para los umbrales de FFMI
FFMI_UMBRAL_HOMBRES = [18, 19, 20, 21, 22.5, 24, 25.5, 27, 29]
FFMI_UMBRAL_MUJERES = [13.5, 14.5, 16, 17, 18.5, 20, 21, 22, 23]


def interpretar_ffmi(ffmi: float, genero: str) -> str:
    """
    Proporciona una interpretación del FFMI basado en rangos preestablecidos que varían según el género.

    Args:
        ffmi (float): Valor del FFMI a interpretar.
        genero (str): Género del usuario ('h' para hombres, 'm' para mujeres).

    Returns:
        str: Descripción del nivel de forma física basado en el FFMI.

    Raises:
        ValueError: Si el valor de 'genero' no es 'h' o 'm'.
    """
    # Validación del género
    if genero not in ['h', 'm']:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")

    # Interpretación del FFMI basada en género
    if genero == 'h':
        if ffmi < FFMI_UMBRAL_HOMBRES[0]:
            return "Lejos del máximo potencial (pobre forma física)"
        elif FFMI_UMBRAL_HOMBRES[0] <= ffmi < FFMI_UMBRAL_HOMBRES[1]:
            return "Cercano a la normalidad"
        elif FFMI_UMBRAL_HOMBRES[1] <= ffmi < FFMI_UMBRAL_HOMBRES[2]:
            return "Normal"
        elif FFMI_UMBRAL_HOMBRES[2] <= ffmi < FFMI_UMBRAL_HOMBRES[3]:
            return "Superior a la normalidad (buena forma física)"
        elif FFMI_UMBRAL_HOMBRES[3] <= ffmi < FFMI_UMBRAL_HOMBRES[4]:
            return "Fuerte (Muy buena forma física)"
        elif FFMI_UMBRAL_HOMBRES[4] <= ffmi < FFMI_UMBRAL_HOMBRES[5]:
            return "Muy fuerte (Excelente forma física). Cerca del máximo potencial."
        elif FFMI_UMBRAL_HOMBRES[5] <= ffmi < FFMI_UMBRAL_HOMBRES[6]:
            return "Muy cerca del máximo potencial."
        elif FFMI_UMBRAL_HOMBRES[6] <= ffmi < FFMI_UMBRAL_HOMBRES[7]:
            return "Potencial máximo natural alcanzado. Muy muy pocos llegan naturales"
        elif FFMI_UMBRAL_HOMBRES[7] <= ffmi < FFMI_UMBRAL_HOMBRES[8]:
            return "Prácticamente imposible sin fármacos"
        else:
            return "Imposible sin fármacos"
    else:  # genero == 'm'
        if ffmi < FFMI_UMBRAL_MUJERES[0]:
            return "Lejos del máximo potencial (pobre forma física)"
        elif FFMI_UMBRAL_MUJERES[0] <= ffmi < FFMI_UMBRAL_MUJERES[1]:
            return "Cercano a la normalidad"
        elif FFMI_UMBRAL_MUJERES[1] <= ffmi < FFMI_UMBRAL_MUJERES[2]:
            return "Normal"
        elif FFMI_UMBRAL_MUJERES[2] <= ffmi < FFMI_UMBRAL_MUJERES[3]:
            return "Superior a la normalidad (buena forma física)"
        elif FFMI_UMBRAL_MUJERES[3] <= ffmi < FFMI_UMBRAL_MUJERES[4]:
            return "Fuerte (Muy buena forma física)"
        elif FFMI_UMBRAL_MUJERES[4] <= ffmi < FFMI_UMBRAL_MUJERES[5]:
            return "Muy fuerte (Excelente forma física). Cerca del máximo potencial."
        elif FFMI_UMBRAL_MUJERES[5] <= ffmi < FFMI_UMBRAL_MUJERES[6]:
            return "Muy cerca del máximo potencial."
        elif FFMI_UMBRAL_MUJERES[6] <= ffmi < FFMI_UMBRAL_MUJERES[7]:
            return "Potencial máximo natural alcanzado. Muy muy pocos llegan naturales"
        elif FFMI_UMBRAL_MUJERES[7] <= ffmi < FFMI_UMBRAL_MUJERES[8]:
            return "Prácticamente imposible sin fármacos"
        else:
            return "Imposible sin fármacos"


# Constantes para los umbrales de relación cintura-cadera

RCC_ALTO_HOMBRES = 0.95
RCC_MODERADO_HOMBRES = 0.90
RCC_ALTO_MUJERES = 0.85
RCC_MODERADO_MUJERES = 0.80


def interpretar_rcc(rcc: float, genero: str) -> str:
    """
    Interpreta la relación cintura-cadera basándose en umbrales específicos
    de riesgo según el género.

    Args:
        rcc (float): Relación cintura-cadera calculada.
        genero (str): Género del usuario ('h' para hombre, 'm' para mujer).

    Returns:
        str: Interpretación del nivel de riesgo asociado con la RCC.

    Raises:
        ValueError: Si el valor de 'genero' no es 'h' o 'm'.
    """
    # Validación del género
    if genero not in ['h', 'm']:
        raise ValueError("El valor de 'genero' debe ser 'h' o 'm'.")

    # Interpretación del RCC basada en género
    if genero == 'h':
        if rcc > RCC_ALTO_HOMBRES:
            return "Alto riesgo"
        elif RCC_MODERADO_HOMBRES < rcc <= RCC_ALTO_HOMBRES:
            return "Moderado riesgo"
        else:
            return "Bajo riesgo"
    else:  # genero == 'm'
        if rcc > RCC_ALTO_MUJERES:
            return "Alto riesgo"
        elif RCC_MODERADO_MUJERES < rcc <= RCC_ALTO_MUJERES:
            return "Moderado riesgo"
        else:
            return "Bajo riesgo"


# Constantes para los umbrales del ratio cintura-altura
RATIO_ALTO_RIESGO = 0.6
RATIO_MODERADO_RIESGO = 0.5


def interpretar_ratio_cintura_altura(ratio: float) -> str:
    """
    Interpreta el ratio cintura-altura para evaluar el riesgo metabólico y posibles riesgos cardiovasculares.

    Args:
        ratio (float): Ratio cintura-altura calculado.

    Returns:
        str: Interpretación del nivel de riesgo metabólico basado en el ratio.

    Raises:
        ValueError: Si el valor de 'ratio' no es positivo.
    """
    # Validación del ratio
    if ratio <= 0:
        raise ValueError("El valor del 'ratio' debe ser un número positivo.")

    # Interpretación del ratio cintura-altura
    if ratio >= RATIO_ALTO_RIESGO:
        return "Alto riesgo"
    elif RATIO_MODERADO_RIESGO <= ratio < RATIO_ALTO_RIESGO:
        return "Moderado riesgo"
    else:
        return "Bajo riesgo"
