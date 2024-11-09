import requests as rq
import json

url = "http://127.0.0.1:5000/informe_completo"

data = {
    "peso": 70,
    "altura": 170,
    "edad": 30,
    "genero": "m",
    "cuello": 35,
    "cintura": 75,
    "cadera": 95,
    "objetivo": "ganar masa muscular",  # Cambiamos según el objetivo que quieras probar
}

response = rq.post(url, json=data)
formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(formatted_json)
