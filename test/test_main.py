import pytest
from fastapi.testclient import TestClient
import sys
import os

# Agregar el directorio padre al path para importar main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_api_running():
    """Test para verificar que la API está funcionando"""
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "API is working"}

def test_predict_survival_female_second_class():
    """Test predicción: mujer de segunda clase (probablemente sobrevive)"""
    body = {
        "edad": 56,
        "clase": "second",
        "sexo": "f"
    }
    response = client.post("/predict", json=body)
    assert response.status_code == 200
    assert "nivel de salades" in response.json()
    print(f"Predicción: {response.json()}")