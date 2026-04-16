# vendas_service.py
from app.service.vendas import Vendas
from app.models.vendedor import Vendedor
class VendasService(Vendas):
    def __init__(self, vendedor: Vendedor):
        self.vendedor = vendedor

    def vender(self, produtos):
        for produto in produtos:
            self.vendedor.adicionar_produto(produto)

        # 🔥 soma total dos produtos vendidos
        total = sum(p.preco for p in self.vendedor.produtos)

        # 🔥 lista de produtos vendidos
        lista_produtos = ", ".join(
            f"{p.nome} (R${p.preco:.2f})"
            for p in self.vendedor.produtos
        )

        return (
            f"Venda realizada por {self.vendedor.nome}\n"
            f"Produtos vendidos: {lista_produtos}\n"
            f"Total vendido: R${total:.2f}"
        )