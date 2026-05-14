# app/remote/request.py
class Request:
    def __init__(self, object_reference, method_name, args):
        self.object_reference = object_reference
        self.method_name = method_name
        self.args = args