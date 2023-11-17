import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.responses import JSONResponse
# from BankNotes  import BankNote1

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

result = ['Fake Note', 'Real Note']

class BankNote1(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/{name}")
def get(name: str):
    return {"Welcome to my First API ": f"{name}"}


@app.post('/predict')
def predict(data: BankNote1):
    prediction_data = [
        data.variance,
        data.skewness,
        data.curtosis,
        data.entropy
    ]

    prediction = classifier.predict([prediction_data])

    return {
        'prediction': result[int(prediction[0])]
    }
#     prediction_result = {"prediction": result[int(prediction_value[0])]}
    
#     return JSONResponse(content=prediction_result)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)