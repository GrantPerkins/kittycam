import cv2

def get_camera():
    camera = cv2.VideoCapture("/dev/video0")
    return camera

def generate_frames(camera):
    while True:
        success, frame = camera.read()

        if not success:
            continue

        ret, buffer = cv2.imencode(
            ".jpg",
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 90]
        )

        if not ret:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" +
            buffer.tobytes() +
            b"\r\n"
        )


