import unittest

from src.body_analyzer.calculos import calcular_macronutrientes
from src.body_analyzer.model import ObjetivoNutricional


class TestCalcularMacronutrientes(unittest.TestCase):

    def test_mantener_peso(self):
        resultado = calcular_macronutrientes(2000, ObjetivoNutricional.MANTENER_PESO)
        esperado = (150.0, 200.0, 66.67)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_perder_grasa(self):
        resultado = calcular_macronutrientes(2000, ObjetivoNutricional.PERDER_GRASA)
        esperado = (200.0, 200.0, 44.44)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_ganar_masa_muscular(self):
        resultado = calcular_macronutrientes(2000, ObjetivoNutricional.GANAR_MASA_MUSCULAR)
        esperado = (150.0, 250.0, 44.44)  # Aproximado
        self.assertAlmostEqual(resultado[0], esperado[0], places=2)
        self.assertAlmostEqual(resultado[1], esperado[1], places=2)
        self.assertAlmostEqual(resultado[2], esperado[2], places=2)

    def test_objetivo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_macronutrientes(2000, 'perder peso rapido')


if __name__ == '__main__':
    unittest.main()
