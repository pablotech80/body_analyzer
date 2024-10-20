import unittest

from src.body_analyzer.model import Sexo, ObjetivoNutricional


class TestEnums(unittest.TestCase):

    def test_sexo_values(self):
        # Comprobar que los valores del Enum Sexo son correctos
        self.assertEqual(Sexo.HOMBRE.value, 'h')
        self.assertEqual(Sexo.MUJER.value, 'm')

    def test_objetivo_nutricional_values(self):
        # Comprobar que los valores del Enum ObjetivoNutricional son correctos
        self.assertEqual(ObjetivoNutricional.MANTENER_PESO.value, 'mantener peso')
        self.assertEqual(ObjetivoNutricional.PERDER_GRASA.value, 'perder grasa')
        self.assertEqual(ObjetivoNutricional.GANAR_MASA_MUSCULAR.value, 'ganar masa muscular')

    def test_enum_membership_sexo(self):
        # Comprobar que ciertos valores están en el enum Sexo
        self.assertIn(Sexo.HOMBRE, Sexo)
        self.assertIn(Sexo.MUJER, Sexo)

    def test_enum_membership_objetivo_nutricional(self):
        # Comprobar que ciertos valores están en el enum ObjetivoNutricional
        self.assertIn(ObjetivoNutricional.MANTENER_PESO, ObjetivoNutricional)
        self.assertIn(ObjetivoNutricional.PERDER_GRASA, ObjetivoNutricional)
        self.assertIn(ObjetivoNutricional.GANAR_MASA_MUSCULAR, ObjetivoNutricional)

    def test_invalid_sexo(self):
        # Comprobar que un valor no válido no pertenece al Enum Sexo
        with self.assertRaises(ValueError):
            Sexo('x')

    def test_invalid_objetivo_nutricional(self):
        # Comprobar que un valor no válido no pertenece al Enum ObjetivoNutricional
        with self.assertRaises(ValueError):
            ObjetivoNutricional('bajar peso')


if __name__ == '__main__':
    unittest.main()
