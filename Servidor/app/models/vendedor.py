# app/models/vendedor.py
class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def total_vendido(self):
        return sum(p.preco for p in self.produtos)