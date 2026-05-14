# app/remote/response.py
class Response:
    def __init__(self, status, result):
        self.status = status
        self.result = result