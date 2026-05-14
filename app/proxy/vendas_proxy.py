# app/proxy/vendas_proxy.py

import socket
import json

from app.remote.request import Request
from app.remote.remote_object_ref import RemoteObjectRef


HOST = "localhost"
PORT = 6000


class VendasProxy:

    def __init__(self):

        self.remote_ref = RemoteObjectRef(
            "VendasService"
        )

    def _send_request(self, method_name, args):

        # 🔹 cria request
        request = Request(
            self.remote_ref,
            method_name,
            args
        )

        # 🔹 serializa request
        request_data = {
            "object_name": request.object_reference.object_name,
            "method_name": request.method_name,
            "args": request.args
        }

        # 🔹 abre conexão
        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        client.connect((HOST, PORT))

        # 🔹 envia request
        client.send(
            json.dumps(request_data).encode()
        )

        # 🔹 recebe response
        response_data = client.recv(4096).decode()

        client.close()

        # 🔹 desserializa
        response = json.loads(response_data)

        return response["result"]

    def listar_produtos(self):

        return self._send_request(
            "listar_produtos",
            []
        )

    def buscar_produto(self, produto_id):

        return self._send_request(
            "buscar_produto",
            [produto_id]
        )

    def comprar_produtos(self, ids):

        return self._send_request(
            "comprar_produtos",
            [ids]
        )

    def calcular_total(self, ids):

        return self._send_request(
            "calcular_total",
            [ids]
        )