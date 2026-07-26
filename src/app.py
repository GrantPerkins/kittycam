import logging
from fastapi import FastAPI, Request

from src.services.stream import get_camera, generate_frames
from fastapi.responses import StreamingResponse

app = FastAPI()
camera = get_camera()
logging.basicConfig(level=logging.INFO)

@app.get("/")
async def stream():
    return StreamingResponse(
        generate_frames(camera),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
