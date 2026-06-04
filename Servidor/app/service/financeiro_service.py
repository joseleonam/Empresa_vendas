# SERVIDOR/app/service/financeiro_service.py
from app.service.vendas import Vendas
from app.tuplespace.global_space import space


class FinanceiroService(Vendas):

    def calcular_total(self, ids):

        produtos = [
            t for t in space.listar_tuplas()
            if t[0] == "PRODUTO"
            and t[1] in ids
        ]
        nomes = ", ".join(p[2] for p in produtos)
        total = sum(p[3] for p in produtos)

        return (
            f"Produtos: {nomes}\n"
            f"Total: R${total:.2f}"
        )