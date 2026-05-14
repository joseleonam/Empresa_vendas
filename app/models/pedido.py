# app/models/pedido.py
class Pedido:

    def __init__(self, id, cliente, produtos):
        self.id = id
        self.cliente = cliente
        self.produtos = produtos

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    def resumo(self):

        nomes = ", ".join(
            produto.nome
            for produto in self.produtos
        )

        return (
            f"Pedido #{self.id}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Produtos: {nomes}\n"
            f"Total: R${self.calcular_total():.2f}"
        )