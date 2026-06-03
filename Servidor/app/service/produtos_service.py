# Servidor/app/service/produtos_service.py
from app.service.vendas import Vendas
from data.load_produtos import carregar_produtos

from faker import Faker
fake = Faker("pt_BR")

class ProdutosService(Vendas):
    def __init__(self):
        self.produtos = carregar_produtos()

    # 🔹 LISTAR PRODUTOS
    def listar_produtos(self):

        return "\n".join(
            f"{p.id} - {p.nome} - R${p.preco:.2f}"
            for p in self.produtos
        )

    # 🔹 BUSCAR PRODUTO(S)
    def buscar_produtos(self, ids):

        ids = [int(i) for i in ids]  # 🔥 GARANTE TIPO CORRETO

        encontrados = [
            p for p in self.produtos
            if int(p.id) in ids
        ]

        if not encontrados:

            return []

        return [
            f"{p.id} - {p.nome} - R${p.preco:.2f}"
            for p in encontrados
        ]