import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from src.services.stream import KittyCamera


@asynccontextmanager
async def lifespan(app: FastAPI):
    kitty_cam.start()
    yield
    kitty_cam.stop()

app = FastAPI(lifespan=lifespan)
kitty_cam = KittyCamera()
logging.basicConfig(level=logging.INFO)


@app.get("/")
async def stream():
    return StreamingResponse(
        kitty_cam.stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
