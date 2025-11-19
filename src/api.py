from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os

# Definir a estrutura dos dados de entrada
class InsuranceInput(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str

# Inicializar a aplicação
app = FastAPI(title="Insurance Cost Prediction API")

# Carregar o modelo treinado
# Carregar o modelo treinado
import os
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models', 'voting_model.joblib')

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Modelo não encontrado em {MODEL_PATH}. Execute o treinamento primeiro.")

model = joblib.load(MODEL_PATH)

@app.get("/")
def read_root():
    return {"message": "API de Previsão de Custos de Seguro está online!"}

@app.post("/predict")
def predict_insurance(data: InsuranceInput):
    try:
        # Converter input para DataFrame (formato esperado pelo pipeline)
        input_data = pd.DataFrame([data.dict()])
        
        # Fazer a predição
        prediction = model.predict(input_data)
        
        return {
            "predicted_charges": float(prediction[0]),
            "input_data": data.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Listar rotas na inicialização para debug
@app.on_event("startup")
async def startup_event():
    print("Rotas disponíveis:")
    for route in app.routes:
        print(f" - {route.path} [{route.methods}]")

if __name__ == "__main__":
    # Executar com reload=True para facilitar desenvolvimento
    # Adicionando diretório atual ao path para que o uvicorn encontre o módulo api
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))
    uvicorn.run("api:app", host="0.0.0.0", port=8005, reload=True)
