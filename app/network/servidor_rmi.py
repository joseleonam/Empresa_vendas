# app/network/servidor_rmi.py

import socket
import json

from app.dispatcher.dispatcher import Dispatcher
from app.service.vendas_service import VendasService
from app.remote.request import Request
from app.remote.remote_object_ref import RemoteObjectRef


HOST = "localhost"
PORT = 6000


def start_server():

    # 🔹 cria dispatcher
    dispatcher = Dispatcher()

    # 🔹 cria serviço remoto
    vendas_service = VendasService()

    # 🔹 registra serviço
    dispatcher.register(
        "VendasService",
        vendas_service
    )

    # 🔹 cria socket servidor
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))

    server.listen(5)

    print(f"[SERVIDOR RMI] Rodando em {HOST}:{PORT}")

    while True:

        conn, addr = server.accept()

        print(f"\nCliente conectado: {addr}")

        try:

            # 🔹 recebe request serializada
            data = conn.recv(4096).decode()

            request_data = json.loads(data)

            # 🔹 reconstruindo request
            request = Request(
                RemoteObjectRef(
                    request_data["object_name"]
                ),
                request_data["method_name"],
                request_data["args"]
            )

            # 🔹 dispatcher executa
            response = dispatcher.dispatch(request)

            # 🔹 serializa response
            response_data = {
                "status": response.status,
                "result": response.result
            }

            conn.send(
                json.dumps(response_data).encode()
            )

        except Exception as e:

            erro = {
                "status": "erro",
                "result": str(e)
            }

            conn.send(
                json.dumps(erro).encode()
            )

        finally:

            conn.close()


if __name__ == "__main__":
    start_server()