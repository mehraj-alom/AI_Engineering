import requests
from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

def get_fact():
    url = "https://meowfacts.herokuapp.com/"
      # Replace with your real API key

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()  # API returns a list of dicts
        fact = data[0]['fact']  # Get the fact from first item


        with open("log/history.txt", "a") as f:
            f.write(fact + "\n")

        return fact

    except Exception as e:
        with open("log/history.txt", "a") as f:
            f.write(f"Error: {str(e)}\n")
        return f"Error: Unable to fetch fact from API - {str(e)}"

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
