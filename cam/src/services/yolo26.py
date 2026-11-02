from typing import cast, Iterator

from ultralytics import YOLO
from ultralytics.engine.results import Results

class YoloCatDetector:
    def __init__(self):
        self._model = YOLO("yolo26n.pt")

    def invoke(self, image):
        results = self._model.predict(image, stream=True)
        results = cast(
            Iterator[Results],
            self._model.predict(image, stream=True)
        )

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                class_id = int(box.cls.item())
                confidence = float(box.conf.item())
                class_name = result.names[class_id].lower()
                # if confidence < 0.25:
                #     return "nothing"
                return class_name+" "+str(confidence)
        return "nothing"

            