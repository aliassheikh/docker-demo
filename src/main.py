from fastapi import FastAPI
from client import RequestClient
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"Welcome": "To the Docker demo"}

@app.get("/get")
def make_request(url: str):
    client = RequestClient()
    return client.get(path=url)

@app.get("/chucknorris")
def chuck_norris_quote():
    client = RequestClient()
    return client.chuck().json()