import json
import unittest

from src.body_analyzer.main import app


class TestMainEndpoints(unittest.TestCase):

    def setUp(self):
        # Configurar la aplicación para pruebas
        self.app = app.test_client()
        self.app.testing = True

    def test_calcular_tmb(self):
        # Caso exitoso
        response = self.app.post(
            "/calcular_tmb",
            data=json.dumps({"peso": 70, "altura": 175, "edad": 30, "genero": "h"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("tmb", json.loads(response.data))

        # Caso con error - faltan parámetros
        response = self.app.post(
            "/calcular_tmb",
            data=json.dumps({"peso": 70, "altura": 175, "edad": 30}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))

    def test_calcular_imc(self):
        # Caso exitoso
        response = self.app.post(
            "/calcular_imc",
            data=json.dumps({"peso": 70, "altura": 175}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("imc", json.loads(response.data))

        # Caso con error - falta parámetro
        response = self.app.post(
            "/calcular_imc",
            data=json.dumps({"peso": 70}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))


    def test_calcular_porcentaje_grasa(self):
        # Caso exitoso para un hombre
        response = self.app.post(
            "/calcular_porcentaje_grasa",
            data=json.dumps(
                {"cintura": 90, "cuello": 40, "altura": 175, "genero": "h"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        try:
            data = json.loads(response.data)
            self.assertIn("porcentaje_grasa", data)
        except json.JSONDecodeError:
            self.fail(f"La respuesta no es un JSON válido: {response.data}")

        # Caso con error - género inválido
        response = self.app.post(
            "/calcular_porcentaje_grasa",
            data=json.dumps(
                {"cintura": 90, "cuello": 40, "altura": 175, "genero": "x"}
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", json.loads(response.data))


if __name__ == "__main__":
    unittest.main()
