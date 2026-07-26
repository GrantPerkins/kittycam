import logging
from fastapi import FastAPI, Request

from src.services.stream import KittyCamera
from fastapi.responses import StreamingResponse

app = FastAPI()
kitty_cam = KittyCamera()
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def stream():
    return StreamingResponse(
        kitty_cam.stream(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
