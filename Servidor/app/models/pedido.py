# SERVIDOR/app/models/pedido.py
class Pedido:

    def __init__(self, id, cliente, vendedor, produtos):
        self.id = id
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = produtos

    def calcular_total(self):

        return sum(
            produto.preco
            for produto in self.produtos
        )

    def resumo(self):

        nomes = ", ".join(p.nome for p in self.produtos)

        return (
            f"PedidoID #{self.id}\n"
            f"ClienteID: {self.cliente.id}\n"
            f"Cliente: {self.cliente.nome}\n"
            f"Vendedor: {self.vendedor.nome}\n"
            f"Produtos: {nomes}\n"
            f"Total: R${self.calcular_total():.2f}"
        )

    def to_tuple(self):

        return (
            "PEDIDO", {
            "Pedido_id": self.id,
            "cliente_id": self.cliente.id,
            "cliente_nome": self.cliente.nome,
            "vendedor": self.vendedor.nome,
            "produtos": [p.nome for p in self.produtos],
            "total": self.calcular_total(),
            "resumo": self.resumo()
        })