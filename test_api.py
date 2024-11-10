import requests
import json

url = "http://127.0.0.1:5000/informe_completo"
data = {
    "peso": 88,
    "altura": 165,
    "edad": 44,
    "genero": "h",
    "cuello": 41,
    "cintura": 90,
    "cadera": 0
}

response = requests.post(url, json=data)
formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(formatted_json)
