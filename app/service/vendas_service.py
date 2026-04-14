# vendas_service.py
from app.service.vendas import Vendas

class VendasService(Vendas):
    def vender(self, produto):
        print(f"Produto vendido: {produto.nome} - R${produto.preco}")