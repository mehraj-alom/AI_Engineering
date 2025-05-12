import requests
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

# Ensure the log directory exists
os.makedirs("log", exist_ok=True)

def get_fact():
    url = "https://meowfacts.herokuapp.com/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        fact = data[0]['fact']

        with open("log/history.txt", "a") as f:
            f.write(fact + "\n")

        return fact

    except Exception as e:
        error_msg = f"Error: Unable to fetch fact from API - {str(e)}"
        with open("log/history.txt", "a") as f:
            f.write(error_msg + "\n")
        return error_msg

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fact")
def read_fact():
    return {"fact": get_fact()}

@app.get("/history")
def read_history():
    try:
        with open("log/history.txt", "r") as f:
            history = f.readlines()
        return {"history": [line.strip() for line in history]}
    except FileNotFoundError:
        return {"history": []}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
