import logging
from fastapi import FastAPI, Request

from src.services.stream import hello_opencv

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def root(request: Request):
    # img = hello_opencv()
    return "hello world!"
