# Servidor/app/service/financeiro_service.py
from app.service.vendas import Vendas
from data.load_produtos import carregar_produtos

from faker import Faker
fake = Faker("pt_BR")

class FinanceiroService(Vendas):
    def __init__(self):
        self.produtos = carregar_produtos()

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