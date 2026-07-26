import threading
import time
from datetime import datetime

import cv2

from src.utils.logger import get_logger


class KittyCamera:
    def __init__(self):
        self.logger = get_logger()

        self.camera = cv2.VideoCapture("/dev/video0")

        if not self.camera.isOpened():
            self.logger.error("failed to open camera")
            raise RuntimeError("Could not open camera: /dev/video0")

        self.running = False
        self.capture_thread: threading.Thread | None = None

        self.latest_jpeg: bytes = b""
        self.condition = threading.Condition()

        # FPS tracking
        self.frame_count = 0
        self.last_fps_time = time.monotonic()
        self.fps = 0.0

    def start(self):
        if self.running:
            return

        self.running = True

        self.capture_thread = threading.Thread(
            target=self._capture_loop,
            name="camera-capture",
            daemon=True,
        )
        self.capture_thread.start()

        self.logger.info("Camera capture thread started")

    def stop(self):
        if not self.running:
            return

        self.running = False

        with self.condition:
            self.condition.notify_all()

        if self.capture_thread is not None:
            self.capture_thread.join()

        self.camera.release()

        self.logger.info("Camera stopped")

    def _capture_loop(self):
        while self.running:
            success, frame = self.camera.read()

            if not success:
                self.logger.error("Failed to read frame from camera")
                continue

            # ---- FPS calculation ----
            self.frame_count += 1

            now = time.monotonic()
            elapsed = now - self.last_fps_time

            if elapsed >= 1.0:
                self.fps = self.frame_count / elapsed
                self.frame_count = 0
                self.last_fps_time = now

            # ---- Overlay timestamp + FPS ----
            overlay_text = (
                f"{datetime.now():%m/%d/%y, %H:%M:%S}    FPS: {self.fps:.1f}"
            )

            position = (5, frame.shape[0] - 5)

            cv2.putText(
                frame,
                overlay_text,
                position,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 0),
                4,
                cv2.LINE_AA,
            )

            cv2.putText(
                frame,
                overlay_text,
                position,
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 255),
                2,
                cv2.LINE_AA,
            )

            # ---- JPEG encode ----
            success, buffer = cv2.imencode(
                ".jpg",
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, 90],
            )

            if not success:
                self.logger.error("Failed to encode frame")
                continue

            jpeg = buffer.tobytes()

            with self.condition:
                self.latest_jpeg = jpeg
                self.condition.notify_all()

    def stream(self):
        while self.running:
            with self.condition:
                self.condition.wait_for(
                    lambda: bool(self.latest_jpeg) or not self.running
                )

                if not self.running:
                    break

                frame = self.latest_jpeg

            yield (
                b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n"
                + frame
                + b"\r\n"
            )
