from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import os

app = FastAPI()
class prediccion(BaseModel):
    edad: int
    clase:str
    sexo: str


with open(os.path.join(os.path.dirname(__file__), "titanic_model.pkl"), 'rb') as f:
    model = pickle.load(f)

@app.post("/predict")
def predict_survival(data: prediccion):
    # Convertir datos de entrada a DataFrame
    input_data = pd.DataFrame([data.model_dump()])

    # Preprocesamiento 
    input_data['sexo'] = input_data['sexo'].map({'male': 0, 'female': 1})
    input_data['clase'] = input_data['clase'].map({'First': 1, 'Second': 2, 'Third': 3})
    input_data = input_data.fillna(input_data.mean())
    features = input_data[['edad', 'clase', 'sexo']]
    prediction = model.predict(features)
    survival = 'De buenas' if prediction[0] == 1 else 'Pailas se muere'
    return {"nivel de salades": survival}

@app.get("/test")
def testApi():
    return {"message": "API is working"}