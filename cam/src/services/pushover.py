import requests
import time

from src.utils.secrets import get_pushover_token_and_userid

class PushNotifications:
    # via Pushover
    def __init__(self):
        self.url = "https://api.pushover.net/1/messages.json"
        self.token, self.userid = get_pushover_token_and_userid()
        self.last = None
        self.frequency_seconds = 60 * 15 # (15 minutes of seconds)

    def __now_seconds(self):
        return time.time()

    def send(self, animal):
        if self.last is None or self.last + self.frequency_seconds > + self.__now_seconds():
            response = requests.post(
                self.url,
                    data={
                        "token": self.token,
                        "user": self.userid,
                        "message": f"{animal} detected on kittycam",
                    },
            )

            response.raise_for_status()
            self.last = self.__now_seconds()
