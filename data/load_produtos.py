from app.models.produto import Celular, Capa, Pelicula, PowerBank


def carregar_produtos():
    produtos = [
        Celular(1, "iPhone 14", 5000, "Apple"),
        Celular(2, "Galaxy S23", 3500, "Samsung"),
        Celular(3, "Moto G84", 2000, "Motorola"),

        Capa(4, "Capa Transparente", 50, "Transparente"),
        Capa(5, "Capa Preta", 40, "Preta"),

        Pelicula(6, "Película 3D", 30, "Vidro"),
        Pelicula(7, "Película Fosca", 25, "Fosca"),

        PowerBank(8, "PowerBank 10000mAh", 120, 10000),
        PowerBank(9, "PowerBank 20000mAh", 180, 20000),
    ]

    return produtos

def produtos_para_dict(produtos):
    lista = []

    for p in produtos:
        lista.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco
        })

    return lista