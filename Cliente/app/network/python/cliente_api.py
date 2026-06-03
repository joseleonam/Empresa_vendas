# Cliente/app/network/python/cliente_api.py

import requests
from app.models.cliente import Cliente
from faker import Faker

fake = Faker("pt_BR")

BASE_URL = "http://localhost:8000"


def criar_cliente_fake():
    cliente = Cliente(
        fake.random_int(min=1, max=999),
        fake.name(),
        fake.email()
    )
    return cliente.to_dict()


def listar_produtos():
    response = requests.get(f"{BASE_URL}/produtos")
    return response.json()


def buscar_produtos(ids: list[int]):
    ids_str = ",".join(map(str, ids))

    response = requests.get(
        f"{BASE_URL}/produtos/buscar",
        params={"ids": ids_str}
    )

    return response.json()


def comprar_produtos(cliente: dict, ids: list[int]):
    payload = {
        "cliente": cliente,
        "ids": ids
    }

    response = requests.post(
        f"{BASE_URL}/compras",
        json=payload
    )

    return response.json()


def calcular_total(ids: list[int]):
    payload = {
        "ids": ids
    }

    response = requests.post(
        f"{BASE_URL}/total",
        json=payload
    )

    return response.json()