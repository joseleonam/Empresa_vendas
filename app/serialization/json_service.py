# json_service.py
import json

class JsonService:

    @staticmethod
    def pack(data: dict) -> bytes:
        json_str = json.dumps(data)
        return json_str.encode()

    @staticmethod
    def unpack(data_bytes: bytes) -> dict:
        json_str = data_bytes.decode()
        return json.loads(json_str)