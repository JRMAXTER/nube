from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI()

DATA =[]

class predictin(BaseModel):
    edad: int
    clase:str
    sexo: str

@app.get("/test")
def read_root():
    return {"message": "que haces aca bro?"}