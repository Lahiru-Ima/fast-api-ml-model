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

sample_data = [
    {
        "id": 1,
        "question": "I couldn't seem to experience any positive feeling at all",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 2,
        "question": "I just couldn't seem to get going",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 3,
        "question": "I felt that I had nothing to look forward to",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 4,
        "question": "I felt sad and depressed",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 5,
        "question": "I felt that I had lost interest in just about everything",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 6,
        "question": "I felt I wasn't worth much as a person",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 7,
        "question": "I felt that life wasn't worthwhile",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 8,
        "question": "I couldn't seem to get any enjoyment out of the things I did",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 9,
        "question": "I felt down-hearted and blue",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 10,
        "question": "I was unable to become enthusiastic about anything",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 11,
        "question": "I felt I was pretty worthless",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 12,
        "question": "I could see nothing in the future to be hopeful about",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 13,
        "question": "I felt that life was meaningless",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 14,
        "question": "I found it difficult to work up the initiative to do things",
        "options": ['Never', 'Sometimes', 'Often', 'Almost always'],
    },
    {
        "id": 15,
        "question": "Education",
        "options": [
            'No school',
            'Less than high school',
            'High school',
            'University degree',
            'Graduate degree'
        ],
    },
    {
        "id": 16,
        "question": "Gender",
        "options": ['Male', 'Female', 'Other'],
    },
    {
        "id": 17,
        "question": "Martial Status",
        "options": ['Never married', 'Currently married', 'Previously married'],
    },
    {
        "id": 18,
        "question": "Age",
        "options": [
            'Primary Children',
            'Secondary Children',
            'Adults',
            'Elder Adults',
            'Older People'
        ],
    },

]


class Answer(BaseModel):
    id: int
    question: str
    options: List[str] = []


class Question(BaseModel):
    question1: int
    question2: int
    question3: int
    question4: int
    question5: int
    question6: int
    question7: int
    question8: int
    question9: int
    question10: int
    question11: int
    question12: int
    question13: int
    question14: int
    question15: int
    question16: int
    question17: int
    question18: int


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


@app.get("/")
def get_question():
    return sample_data


@app.get("/{id}")
def get_one_question(id: int):
    return sample_data[id-1]


@app.post("/")
def create_question(answer:  List[int]):
    # answers = question.dict()
    # feature_list = [answer for answer in answers.values()]
    pred_value = prediction(answer)
    return pred_value
    # return answer

# if __name__ == "__main__":
#     uvicorn.run(app,host='127.0.0.1',port=8000)
