from xmlrpc.server import SimpleXMLRPCServer

from app.service.vendas_service import VendasService

HOST = "localhost"
PORT = 6000

server = SimpleXMLRPCServer(
    (HOST, PORT),
    allow_none=True
)

service = VendasService()

server.register_function(
    service.listar_produtos,
    "listar_produtos"
)

server.register_function(
    service.buscar_produtos,
    "buscar_produtos"
)

server.register_function(
    service.comprar_produtos,
    "comprar_produtos"
)

server.register_function(
    service.calcular_total,
    "calcular_total"
)

print(f"Servidor RMI rodando em {HOST}:{PORT}")

server.serve_forever()