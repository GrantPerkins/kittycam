import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from src.services.stream import KittyCamera


app = FastAPI()
kitty_cam = KittyCamera()
logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    kitty_cam.start()
    yield
    kitty_cam.stop()

@app.get("/")
async def stream():
    return StreamingResponse(
        kitty_cam.stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
