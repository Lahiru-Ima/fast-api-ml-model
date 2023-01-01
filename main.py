

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


class Question(BaseModel):
    question1:int 
    question2:int
    question3:int
    question4:int
    question5:int
    question6:int
    question7:int
    question8:int
    question9:int
    question10:int
    question11:int
    question12:int
    question13:int
    question14:int
    question15:int
    question16:int
    question17:int
    question18:int

def prediction(lst):
    model = joblib.load("dep_predict_model.pickle")
    # filename = 'dep_predict_model.pickle'
    # with open(filename,'rb') as file:
    #     model = pickle.load(file)
    pred_value = model.predict([lst])
    # return pred_value
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
def get_question(question:Question):
    answers =  question.dict()
    feature_list = [answer for answer in answers.values()]
    pred_value = prediction(feature_list)
    return pred_value

# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=8000)
