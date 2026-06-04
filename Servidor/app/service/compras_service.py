# Servidor/app/service/compras_service.py

from app.service.vendas import Vendas
from app.tuplespace.global_space import space


class ComprasService(Vendas):

    def comprar_produtos(
        self,
        cliente,
        ids
    ):

        space.write(
            (
                "COMPRA",
                cliente,
                ids
            )
        )

        return {
            "status":
            "Compra enviada para o espaço de tuplas"
        }
    
    def buscar_pedido(self, cliente_id: int):
        
        pedidos = []
        while True:
            pedido = space.take_pedido_cliente(
                cliente_id
            )

            if pedido:
                pedidos.append(pedido["resumo"])
            else:
                break

        if pedidos:
            return pedidos

        return {
            "status": "Nenhum pedido encontrado"
        }