# produto.py
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco


class Celular(Produto):
    def __init__(self, id, nome, preco, marca):
        super().__init__(id, nome, preco)
        self.marca = marca


class Capa(Produto):
    def __init__(self, id, nome, preco, cor):
        super().__init__(id, nome, preco)
        self.cor = cor


class Pelicula(Produto):
    def __init__(self, id, nome, preco, tipo):
        super().__init__(id, nome, preco)
        self.tipo = tipo


class PowerBank(Produto):
    def __init__(self, id, nome, preco, capacidade):
        super().__init__(id, nome, preco)
        self.capacidade = capacidade