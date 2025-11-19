from fastapi.testclient import TestClient
from app import app
import json

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de Previsão de Custos de Seguro está online!"}
    print("Teste Root: OK")

def test_predict():
    payload = {
        "age": 30,
        "sex": "male",
        "bmi": 25.5,
        "children": 0,
        "smoker": "no",
        "region": "southwest"
    }
    
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    print(f"Status Code: {response.status_code}")
    print(f"Resposta: {json.dumps(data, indent=2)}")
    
    assert "predicted_charges" in data
    assert isinstance(data["predicted_charges"], float)
    print("Teste Predict: OK")

if __name__ == "__main__":
    print("Iniciando testes...")
    test_read_root()
    test_predict()
    print("Todos os testes passaram!")
