# SERVIDOR/app/service/produtos_service.py
from app.service.vendas import Vendas
from data.load_produtos import carregar_produtos
from app.tuplespace.global_space import space


class ProdutosService(Vendas):

    def __init__(self):

        self.produtos = carregar_produtos()

        if not space.read("PRODUTO"):

            for produto in self.produtos:
                space.write(
                    (
                        "PRODUTO",
                        produto.id,
                        produto.nome,
                        produto.preco
                    )
                )

    def listar_produtos(self):

        produtos = [
            t for t in space.listar_tuplas()
            if t[0] == "PRODUTO"
        ]

        return "\n".join(
            f"{id} - {nome} - R${preco:.2f}"
            for _, id, nome, preco in produtos
        )

    def buscar_produtos(self, ids):

        encontrados = [
            t for t in space.listar_tuplas()
            if t[0] == "PRODUTO"
            and t[1] in ids
        ]

        return "\n".join(
            f"{id} - {nome} - R${preco:.2f}"
            for _, id, nome, preco in encontrados
        )