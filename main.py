from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Answers(BaseModel):
    id: int
    question: str
    options: List[str] = []

def prediction(lst):
    model = joblib.load("dep_predict_model.pickle")
    pred_value = model.predict([lst])
    if pred_value == [4]:
            return 'Extremely Severe'
    elif pred_value == [3]:
        return 'Severe'
    elif pred_value == [2]:
        return 'Moderate'
    elif pred_value == [1]:
        return 'Mild'
    elif pred_value == [0]:
        return 'Normal'
    else:
        return 'None'

@app.post("/")
def create_question(answers: List[int]):
    pred_value = prediction(answers)
    return pred_value
