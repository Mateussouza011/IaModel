from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import uvicorn
import os
import tensorflow as tf
from contextlib import asynccontextmanager

# Detecta o diretório base (funciona local e no Railway)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
MODEL1_PATH = os.path.join(MODELS_DIR, 'model1.keras')
MODEL2_PATH = os.path.join(MODELS_DIR, 'model2.keras')
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, 'preprocessor.joblib')

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        if os.path.exists(MODEL1_PATH) and os.path.exists(MODEL2_PATH) and os.path.exists(PREPROCESSOR_PATH):
            print("Loading models and preprocessor...")
            models["model1"] = tf.keras.models.load_model(MODEL1_PATH)
            models["model2"] = tf.keras.models.load_model(MODEL2_PATH)
            models["preprocessor"] = joblib.load(PREPROCESSOR_PATH)
            print("Models loaded successfully!")
        else:
            print("WARNING: Models not found. Please run training script first.")
    except Exception as e:
        print(f"Error loading models: {e}")
    
    yield
    
    models.clear()

app = FastAPI(title="Diamonds Price Prediction API", lifespan=lifespan)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DiamondInput(BaseModel):
    carat: float
    cut: str
    color: str
    clarity: str
    depth: float
    table: float
    x: float
    y: float
    z: float

@app.get("/")
def read_root():
    return {"message": "Diamonds Price Prediction API is online!"}

@app.post("/predict")
def predict_price(data: DiamondInput):
    if not models.get("model1") or not models.get("model2") or not models.get("preprocessor"):
        raise HTTPException(status_code=503, detail="Models not loaded. Service unavailable.")
    
    try:
        input_df = pd.DataFrame([data.dict()])
        
        processed_data = models["preprocessor"].transform(input_df)
        
        pred1 = models["model1"].predict(processed_data).flatten()[0]
        pred2 = models["model2"].predict(processed_data).flatten()[0]
        
        final_prediction = (pred1 + pred2) / 2
        
        return {
            "predicted_price": float(final_prediction),
            "details": {
                "model1": float(pred1),
                "model2": float(pred2)
            },
            "input": data.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == "__main__":
    import sys
    sys.path.append(os.path.dirname(__file__))
    uvicorn.run("api:app", host="0.0.0.0", port=8005, reload=False)
