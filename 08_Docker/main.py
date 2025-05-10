from fastapi import FastAPI
from verific import Data
import pickle
import uvicorn
app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/model")
def predict(data: Data):
    x1 = data.x1
    x2 = data.x2
    result = model.predict([[x1, x2]])
    return {"result": result[0]}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
   
