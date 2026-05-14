# app/serialization/json_serializer.py
import json

class JsonSerializer:

    @staticmethod
    def serialize(obj):
        return json.dumps(obj.__dict__)

    @staticmethod
    def deserialize(data):
        return json.loads(data)