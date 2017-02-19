from globals import REQUEST_URL
import requests


class Sender:
    def send(self):
        requests.post(REQUEST_URL + self.method, data=self.data)

    def __init__(self, data):
        self.data = data.data
        self.method = data.method
