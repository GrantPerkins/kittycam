import cv2
import numpy as np
import base64

def hello_opencv():
    # Create a black background image (300 height, 400 width, 3 color channels)
    img = np.zeros((300, 400, 3), dtype=np.uint8)

    # Add "Hello World" text to the image
    cv2.putText(
        img,
        "Hello World",
        (50, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )
    encoded_bytes = base64.b64encode(img)
    return encoded_bytes

