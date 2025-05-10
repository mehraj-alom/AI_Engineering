from fastapi import FastAPI
from pydan import get_pydan
import pickle
import uvicorn
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
with open("model.pkl","rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: get_pydan):
    x1 = data.x1
    x2 = data.x2
    result = model.predict([[x1, x2]])
    # Log the prediction
    with open("logs/prediction.txt","a") as f:
        f.write(f"{x1} {x2} Prediction: {result}\n")
    return {"prediction": result[0]}

@app.get("/logs")
def get_logs():
    try:
        with open("logs/prediction.txt", "r") as f:
            log_contents = f.read()
        return {"logs": log_contents}
    except FileNotFoundError:
        return {"logs": "Log file not found."}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)

