import unittest

from src.body_analyzer.calculos import (
    calcular_macronutrientes,
    calcular_porcentaje_grasa,
)
from src.body_analyzer.model import ObjetivoNutricional, Sexo


class TestCalcularMacronutrientes(unittest.TestCase):

    def test_mantener_peso(self):
        """Prueba para mantener el peso con 2000 calorías diarias."""
        resultado = calcular_macronutrientes(2000, ObjetivoNutricional.MANTENER_PESO)
        esperado = (150.0, 200.0, 66.67)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_perder_grasa(self):
        """Prueba para perder grasa con 2000 calorías diarias."""
        resultado = calcular_macronutrientes(2000, ObjetivoNutricional.PERDER_GRASA)
        esperado = (200.0, 200.0, 44.44)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_ganar_masa_muscular(self):
        """Prueba para ganar masa muscular con 2000 calorías diarias."""
        resultado = calcular_macronutrientes(
            2000, ObjetivoNutricional.GANAR_MASA_MUSCULAR
        )
        esperado = (150.0, 250.0, 44.44)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_objetivo_invalido(self):
        """Prueba para manejar un objetivo nutricional inválido."""
        with self.assertRaises(ValueError):
            calcular_macronutrientes(2000, "perder peso rapido")

    def test_calcular_porcentaje_grasa_hombre(self):
        """Prueba del cálculo de porcentaje de grasa corporal para un hombre."""
        # Datos de prueba
        altura = 165
        cuello = 41
        cintura = 98
        cadera = None  # No se usa para hombres
        genero = Sexo.HOMBRE

        # Valor esperado aproximado
        resultado_esperado = 25.89

        # Llamada a la función
        resultado = calcular_porcentaje_grasa(cintura, cuello, altura, genero, cadera)

        self.assertAlmostEqual(resultado, resultado_esperado, places=2)

    def test_calcular_porcentaje_grasa_mujer(self):
        """Prueba del cálculo de porcentaje de grasa corporal para una mujer."""
        # Datos de prueba
        altura = 170
        cuello = 37
        cintura = 75
        cadera = 100
        genero = Sexo.MUJER

        # Valor esperado aproximado
        resultado_esperado = 26.11

        # Llamada a la función
        resultado = calcular_porcentaje_grasa(cintura, cuello, altura, genero, cadera)

        self.assertAlmostEqual(resultado, resultado_esperado, places=2)


if __name__ == "__main__":
    unittest.main()
