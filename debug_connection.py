import requests
import json

API_URL = "http://127.0.0.1:8000/predict"
ROOT_URL = "http://127.0.0.1:8000/"

print(f"Testando conexão com {ROOT_URL}...")
try:
    response = requests.get(ROOT_URL)
    print(f"Status Root: {response.status_code}")
    print(f"Response Root: {response.text}")
except Exception as e:
    print(f"Erro ao conectar no Root: {e}")

print(f"\nTestando POST em {API_URL}...")
payload = {
    "age": 30,
    "sex": "male",
    "bmi": 25.5,
    "children": 0,
    "smoker": "no",
    "region": "southwest"
}

try:
    response = requests.post(API_URL, json=payload)
    print(f"Status Predict: {response.status_code}")
    print(f"Response Predict: {response.text}")
    
    if response.status_code == 404:
        print("\nALERTA: Erro 404 detectado.")
        print("Verifique se a URL está correta e se o endpoint /predict aceita POST.")
        
except Exception as e:
    print(f"Erro ao conectar no Predict: {e}")
