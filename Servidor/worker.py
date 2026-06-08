# Servidor/worker.py

from app.tuplespace.global_space import space
from data.load_produtos import carregar_produtos

from app.models.vendedor import Vendedor
from app.models.cliente import Cliente
from app.models.pedido import Pedido

from faker import Faker

import time

fake = Faker("pt_BR")

produtos = carregar_produtos()

while True:

    compra = space.take("COMPRA")

    if compra:

        _, cliente_data, ids = compra

        encontrados = []

        for id_produto in ids:

            produto = next(
                (
                    p for p in produtos
                    if p.id == id_produto
                ),
                None
            )

            if produto:
                encontrados.append(produto)

        if encontrados:

            cliente = Cliente(
                cliente_data["id"],
                cliente_data["nome"],
                cliente_data["email"]
            )

            vendedor = Vendedor(
                fake.name()
            )

            for produto in encontrados:
                vendedor.adicionar_produto(
                    produto
                )

            pedido = Pedido(
                fake.random_int(
                    min=1,
                    max=999
                ),
                cliente,
                vendedor,
                encontrados
            )


            print(
                "\n=== PEDIDO PROCESSADO ==="
            )

            print(pedido.resumo())

            space.write(
                (pedido.to_tuple())
            )

    time.sleep(2)