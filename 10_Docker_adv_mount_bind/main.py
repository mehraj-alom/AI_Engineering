from fastapi import FastAPI
from Inputdata import Inputdata
import pickle 
import uvicorn

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/predict")
def predict(data: Inputdata):
    x1 = data.x1
    x2 = data.x2
    result = model.predict([[x1, x2]])
    # Log the prediction
    with open("logs/prediction.txt", "a") as f:
        f.write(f"{x1} {x2} Prediction: {result}\n")
    return {"prediction": result[0]}
@app.post("/add")
def add(x: int, y: int):
    return {"result": x + y}

@app.get("/logs")
def get_logs():
    try:
        with open ("logs/prediction.txt", "r") as f:
            log_contents = f.read()
        return {"logs": log_contents}
    except FileNotFoundError:
        return {"logs": "Log file not found."}
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



#Mount Bind :: 
# docker run \
#   --rm \
#   -v /home/myspace/vsenvs/learn-env/AI_Engineering/10_Docker_adv_mount_bind:/application \
#   -w /application \
#   -p 8000:8000 \
#   fe5cfacf60c0 \
#   uvicorn main:app --host 0.0.0.0 --port 8000 --reload --reload-dir /application

# We must have to tun reload explicitely in the docker run command beecause 
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# This does not include --reload, and so the FastAPI app inside the container does not automatically reload when you change files on your host, even with volume mounts.