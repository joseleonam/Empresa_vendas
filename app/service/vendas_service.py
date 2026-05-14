# app/service/vendas_service.py
from app.service.vendas import Vendas
from data.load_produtos import carregar_produtos

from app.models.vendedor import Vendedor
from app.models.cliente import Cliente
from app.models.pedido import Pedido


class VendasService(Vendas):
    def __init__(self, vendedor):
        self.vendedor = vendedor
        self.produtos = carregar_produtos()

    # 🔹 LISTAR PRODUTOS
    def listar_produtos(self):

        return "\n".join(
            f"{p.id} - {p.nome} - R${p.preco:.2f}"
            for p in self.produtos
        )

    # 🔹 BUSCAR PRODUTO
    def buscar_produto(self, produto_id):
        for produto in self.produtos:
            if produto.id == produto_id:
                return (
                    f"{produto.id} - "
                    f"{produto.nome} - "
                    f"R${produto.preco:.2f}"
                )

        return "Produto não encontrado"

    # 🔹 COMPRAR PRODUTOS
    def comprar_produtos(self, ids):
        encontrados = [
            p for p in self.produtos
            if p.id in ids
        ]

        if not encontrados:
            return "Nenhum produto encontrado"

        # 🔹 adiciona produtos ao vendedor
        for produto in encontrados:
            self.vendedor.adicionar_produto(
                produto
            )

        # 🔹 cria cliente
        cliente = Cliente(
            1,
            "José",
            "jose@email.com"
        )

        # 🔹 cria pedido
        pedido = Pedido(
            1,
            cliente,
            encontrados
        )

        return pedido.resumo()

    # 🔹 CALCULAR TOTAL
    def calcular_total(self, ids):
        encontrados = [
            p for p in self.produtos
            if p.id in ids
        ]

        total = sum(
            p.preco
            for p in encontrados
        )

        return f"Total: R${total:.2f}"