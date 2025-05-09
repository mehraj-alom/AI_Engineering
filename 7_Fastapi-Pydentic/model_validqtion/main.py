from fastapi import FastAPI
from data_val import Item 
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}

if __name__ == "__main__":

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)