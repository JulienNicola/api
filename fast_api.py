# Library imports
import uvicorn
import gunicorn
from fastapi import FastAPI, Request
import numpy as np
import pickle
import pandas as pd
from zipfile import ZipFile
from pydantic import BaseModel
import os
from fastapi.responses import JSONResponse
from typing import Dict

# Create the app object
app = FastAPI()

#Load the model
pickle_in = open("lgbm.pkl","rb")
classifier=pickle.load(pickle_in)

pickle_in = open("threshold.pkl","rb")
threshold=pickle.load(pickle_in)

class ClientData(BaseModel):
    client_id: int
    features: Dict[str, float]

# make a prediction using client data

@app.post("/predict")
def predict_credit(request: Request, client_data: ClientData):
    features = pd.DataFrame(client_data.features, index=[0])
    
    score = classifier.predict_proba(features)[0][0]
    if score>=threshold:
        decision="accepted"
    else:
        decision="declined"
    return {
        'client_id': client_data.client_id,
        'score': score,
        'decision': decision
    }