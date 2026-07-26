import base64

import requests
import cv2
import numpy as np


response = requests.get("http://localhost:8000")
print(response.text)
# json = response.json()
# img_str = json["message"]
# img_bytes = base64.b64decode(img_str)
# restored_arr = np.frombuffer(img_bytes, dtype=np.uint8).reshape(300, 400, 3)
# cv2.imwrite("response.jpg", restored_arr)
