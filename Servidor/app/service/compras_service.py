# Servidor/app/service/compras_service.py
from app.service.vendas import Vendas
from data.load_produtos import carregar_produtos

from app.models.vendedor import Vendedor
from app.models.cliente import Cliente
from app.models.pedido import Pedido

from faker import Faker
fake = Faker("pt_BR")

class ComprasService(Vendas):
    def __init__(self):
        self.produtos = carregar_produtos()

    # 🔹 COMPRAR PRODUTOS
    def comprar_produtos(self, cliente_data,ids):
        encontrados = [
            p for p in self.produtos
            if p.id in ids
        ]

        if not encontrados:
            return "Nenhum produto encontrado"
        
        # 🔹 reconstrói cliente recebido
        cliente = Cliente(
            cliente_data["id"],
            cliente_data["nome"],
            cliente_data["email"]
        )

        # 🔹 vendedor criado automaticamente
        vendedor = Vendedor(
            fake.name()
        )
        
        # 🔹 adiciona produtos ao vendedor
        for produto in encontrados:
            vendedor.adicionar_produto(
                produto
            )

        # 🔹 cria pedido
        pedido = Pedido(
            fake.random_int(min=1, max=999),
            cliente,
            vendedor,
            encontrados
        )

        return pedido.resumo()