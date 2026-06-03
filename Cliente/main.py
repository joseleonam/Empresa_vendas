# Cliente/app/network/python/main.py

import os
from app.network.python.cliente_api import (
    listar_produtos,
    buscar_produtos,
    comprar_produtos,
    calcular_total,
    criar_cliente_fake
)


def menu():
    print("\n=== SISTEMA DE VENDAS (API/PYTHON) ===")
    print("1 - Listar produtos")
    print("2 - Buscar produtos")
    print("3 - Comprar produtos")
    print("4 - Calcular total")
    print("0 - Sair")

    return input("Escolha: ")

def limpar_tela():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )
    
def main():

    cliente = criar_cliente_fake()

    while True:

        opcao = menu()

        if opcao == "1":
            limpar_tela()
            print("\n=== PRODUTOS ===")
            print(listar_produtos())

        elif opcao == "2":
            ids = input("IDs (ex: 1,2,3): ")
            lista = [int(x.strip()) for x in ids.split(",")]
            limpar_tela()
            print("\n=== RESULTADO ===")
            print(buscar_produtos(lista))

        elif opcao == "3":
            ids = input("IDs (ex: 1,2,3): ")
            lista = [int(x.strip()) for x in ids.split(",")]
            limpar_tela()
            print("\n=== COMPRA ===")
            print(comprar_produtos(cliente, lista))

        elif opcao == "4":
            ids = input("IDs (ex: 1,2,3): ")
            lista = [int(x.strip()) for x in ids.split(",")]
            limpar_tela()
            print("\n=== TOTAL ===")
            print(calcular_total(lista))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()