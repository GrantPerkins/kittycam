import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, FileResponse

from src.services.yolo26 import YoloCatDetector
from src.services.stream import KittyCamera
from src.middleware.jwt import CloudflareAccessMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    kitty_cam.start()
    try:
        yield
    finally:
        kitty_cam.stop()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CloudflareAccessMiddleware,
    exempt_paths={
        "/manifest.json",
    },
)

cat_detector = YoloCatDetector()
kitty_cam = KittyCamera(cat_detector=cat_detector)
logging.basicConfig(level=logging.INFO)


@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/manifest.json")
async def manifest():
    return FileResponse("static/manifest.json")


@app.get("/stream")
async def stream(request: Request):
    return StreamingResponse(
        kitty_cam.stream(request),
        media_type="multipart/x-mixed-replace; boundary=frame",
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
