



def interpretar_imc(imc, ffmi, genero):

    """Interpreta el resultado del IMC considerando el FFMI.

        Args:
            imc (float): Índice de Masa Corporal calculado.
            ffmi (float): Índice de Masa Libre de Grasa.
            genero (str): Género del usuario.

        Returns:
            str: Interpretación del IMC basada en los valores de FFMI y género.
        """
    if imc > 25 and ffmi > 19 if genero == 'm' else ffmi > 16:
        return "El IMC es alto, pero puede estar influenciado por una alta masa muscular."
    elif imc < 18.5:
        return "El IMC es bajo, se recomienda consultar con un profesional de salud."
    else:
        return "El IMC está dentro del rango normal."


def interpretar_porcentaje_grasa(porcentaje_grasa, genero):

    """
        Interpreta el porcentaje de grasa corporal basándose en el género y proporciona una evaluación cualitativa.

        Args:
            porcentaje_grasa (float): El porcentaje de grasa corporal calculado.
            genero (str): El género del individuo ('h' para hombres, 'm' para mujeres).

        Returns:
            str: Una cadena de texto que describe el estado del porcentaje de grasa corporal en términos de salud.
        """
    if genero == 'h':
        if porcentaje_grasa > 25:
            return "Alto"
        elif porcentaje_grasa < 6:
            return "Bajo"
        else:
            return "Normal"
    else:
        if porcentaje_grasa > 32:
            return "Alto"
        elif porcentaje_grasa < 16:
            return "Bajo"
        else:
            return "Normal"

def interpretar_ffmi(ffmi, genero):

    """
        Proporciona una interpretación del FFMI basado en rangos preestablecidos que varían según el género,
        aparte da información sobre los mín y máx de potencial genético según los valores, dando así un
        número superior al máx, uso de fármacos para lograr ese resultado.

        Args:
            ffmi (float): Valor del FFMI a interpretar.
            genero (str): Género del usuario ('h' para hombres, 'm' para mujeres).

        Returns:
            str: Descripción del nivel de forma física basado en el FFMI.
        """
    if genero == 'h':
        if ffmi < 18:
            return "Lejos del máximo potencial (pobre forma física)"
        elif 18 <= ffmi < 19:
            return "Cercano a la normalidad"
        elif 19 <= ffmi < 20:
            return "Normal"
        elif 20 <= ffmi < 21:
            return "Superior a la normalidad (buena forma física)"
        elif 21 <= ffmi < 22.5:
            return "Fuerte (Muy buena forma física)"
        elif 22.5 <= ffmi < 24:
            return "Muy fuerte (Excelente forma física). Cerca del máximo potencial."
        elif 24 <= ffmi < 25.5:
            return "Muy cerca del máximo potencial."
        elif 25.5 <= ffmi < 27:
            return "Potencial máximo natural alcanzado. Muy muy pocos llegan naturales"
        elif 27 <= ffmi < 29:
            return "Prácticamente imposible sin fármacos"
        else:
            return "Imposible sin fármacos"
    else:
        if ffmi < 13.5:
            return "Lejos del máximo potencial (pobre forma física)"
        elif 13.5 <= ffmi < 14.5:
            return "Cercano a la normalidad"
        elif 14.5 <= ffmi < 16:
            return "Normal"
        elif 16 <= ffmi < 17:
            return "Superior a la normalidad (buena forma física)"
        elif 17 <= ffmi < 18.5:
            return "Fuerte (Muy buena forma física)"
        elif 18.5 <= ffmi < 20:
            return "Muy fuerte (Excelente forma física). Cerca del máximo potencial."
        elif 20 <= ffmi < 21:
            return "Muy cerca del máximo potencial."
        elif 21 <= ffmi < 22:
            return "Potencial máximo natural alcanzado. Muy muy pocos llegan naturales"
        elif 22 <= ffmi < 23:
            return "Prácticamente imposible sin fármacos"
        else:
            return "Imposible sin fármacos"


def interpretar_rcc(rcc, genero):

    """Interpreta la relación cintura-cadera basándose en umbrales específicos de riesgo según el género,
        con este dato se sabe que nivel de sobrepeso tiene y si proviene de hipertrofia muscular o acumulación de grasa.

        Args:
            rcc (float): Relación cintura-cadera calculada.
            genero (str): Género del usuario ('h' para hombre, 'm' para mujer).

        Returns:
            str: Interpretación del nivel de riesgo asociado con la RCC.
        """
    if genero == 'h':
        if rcc > 0.95:
            return "Alto riesgo"
        elif 0.90 < rcc <= 0.95:
            return "Moderado riesgo"
        else:
            return "Bajo riesgo"
    else:
        if rcc > 0.85:
            return "Alto riesgo"
        elif 0.80 < rcc <= 0.85:
            return "Moderado riesgo"
        else:
            return "Bajo riesgo"



def interpretar_ratio_cintura_altura(ratio):

    """Interpreta el ratio cintura-altura para evaluar el riesgo metabólico
        y posibles riesgos cardiovasculares

        Args:
            ratio (float): Ratio cintura-altura calculado.

        Returns:
            str: Interpretación del nivel de riesgo metabólico basado en el ratio.
        """
    if ratio >= 0.6:
        return "Alto riesgo"
    elif 0.5 <= ratio < 0.6:
        return "Moderado riesgo"
    else:
        return "Bajo riesgo"

    