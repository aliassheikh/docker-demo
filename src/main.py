from fastapi import FastAPI
from client import RequestClient

app = FastAPI()

@app.get("/")
def read_root():
    return {"Welcome": "To the Docker demo"}

@app.get("/get")
def make_request(path: str):
    client = RequestClient()
    return client.get(path=path)

@app.get("/chucknorris")
def chuck_norris_quote():
    client = RequestClient()
    return client.chuck()