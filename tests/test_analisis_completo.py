import unittest
from src.body_analyzer.analisis_completo import informe_completo

class TestInformeCompleto(unittest.TestCase):
    def test_informe_completo_exitoso_hombre(self):
        data = {
            "peso": 75,
            "altura": 180,
            "edad": 30,
            "genero": "h",
            "cuello": 40,
            "cintura": 90,
        }
        resultado = informe_completo(data)

        self.assertIn("resultados", resultado)
        self.assertIn("interpretaciones", resultado)
        self.assertEqual(len(resultado["resultados"]), 8)
        self.assertEqual(len(resultado["interpretaciones"]), 5)
        self.assertNotIn("error", resultado)

    def test_informe_completo_exitoso_mujer(self):
        data = {
            "peso": 65,
            "altura": 165,
            "edad": 28,
            "genero": "m",
            "cuello": 35,
            "cintura": 70,
            "cadera": 95,
        }
        resultado = informe_completo(data)

        self.assertIn("resultados", resultado)
        self.assertIn("interpretaciones", resultado)
        self.assertEqual(len(resultado["resultados"]), 8)
        self.assertEqual(len(resultado["interpretaciones"]), 5)
        self.assertNotIn("error", resultado)

    def test_faltan_parametros_obligatorios(self):
        data = {
            "peso": 75,
            "altura": 180,
            "genero": "h",
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "Faltan parámetros obligatorios.")

    def test_genero_invalido(self):
        data = {
            "peso": 75,
            "altura": 180,
            "edad": 30,
            "genero": "x",
            "cuello": 40,
            "cintura": 90,
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "El valor de 'genero' debe ser 'h' o 'm': x")

    def test_peso_invalido(self):
        data = {
            "peso": -75,
            "altura": 180,
            "edad": 30,
            "genero": "h",
            "cuello": 40,
            "cintura": 90,
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "El peso debe ser un número positivo.")

    def test_altura_invalida(self):
        data = {
            "peso": 75,
            "altura": -180,
            "edad": 30,
            "genero": "h",
            "cuello": 40,
            "cintura": 90,
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "La altura debe ser un número positivo.")

    def test_edad_invalida(self):
        data = {
            "peso": 75,
            "altura": 180,
            "edad": -30,
            "genero": "h",
            "cuello": 40,
            "cintura": 90,
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "La edad debe ser un número entero positivo.")

    def test_faltan_parametros_para_mujer(self):
        data = {
            "peso": 65,
            "altura": 165,
            "edad": 28,
            "genero": "m",
            "cuello": 35,
            "cintura": 70,
        }
        resultado = informe_completo(data)

        self.assertIn("error", resultado)
        self.assertEqual(resultado["error"], "El valor de 'cadera' debe ser un número positivo para mujeres.")

    def test_parametros_correctos_para_mujer(self):
        data = {
            "peso": 65,
            "altura": 165,
            "edad": 28,
            "genero": "m",
            "cuello": 35,
            "cintura": 70,
            "cadera": 95,
        }
        resultado = informe_completo(data)

        self.assertIn("resultados", resultado)
        self.assertEqual(resultado["resultados"]["rcc"], 0.74)  # Testea el valor RCC
