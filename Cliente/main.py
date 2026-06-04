# Cliente/app/network/python/main.py

import subprocess
import sys
import os
from app.network.python.cliente_api import (
    criar_cliente_fake,
    listar_produtos,
    buscar_produtos,
    comprar_produtos,
    calcular_total,
    buscar_pedido
    
)




def main():

    print("Abrindo cliente em novo terminal...")

    subprocess.Popen(
        [
            "cmd",
            "/c",
            f"{sys.executable} {__file__} cliente"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

def menu():
    print("\n=== SISTEMA DE VENDAS (API/PYTHON) ===")
    print("1 - Listar produtos")
    print("2 - Buscar produtos")
    print("3 - Comprar produtos")
    print("4 - Calcular total")
    print("5 - Buscar pedido")
    print("0 - Sair")

    return input("Escolha: ")

def limpar_tela():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )
    
def executar_cliente():

    cliente = criar_cliente_fake()

    while True:
        print(f"\nClienteID #{cliente['id']}#\nnome: {cliente['nome']}!")
        opcao = menu()

        match opcao:
            case "1":
                limpar_tela()
                print("\n=== PRODUTOS ===")
                print(listar_produtos())

            case "2":
                ids = input("IDs (ex: 1,2,3): ")
                lista = [int(x.strip()) for x in ids.split(",")]
                limpar_tela()
                print("\n=== RESULTADO ===")
                print(buscar_produtos(lista))

            case "3":
                ids = input("IDs (ex: 1,2,3): ")
                lista = [int(x.strip()) for x in ids.split(",")]
                limpar_tela()
                print("\n=== COMPRA ===")
                print(comprar_produtos(cliente, lista))

            case "4":
                ids = input("IDs (ex: 1,2,3): ")
                lista = [int(x.strip()) for x in ids.split(",")]
                limpar_tela()
                print("\n=== TOTAL ===")
                print(calcular_total(lista))

            case "5":
                cliente_id = cliente["id"]
                limpar_tela()
                print("\n=== MEUS PEDIDOS ===")

                pedidos = buscar_pedido(cliente_id)

                if isinstance(pedidos, dict):
                    print(pedidos["status"])
                else:
                    for pedido in pedidos:
                        print(pedido)
                        print("-" * 40)

            case "0":
                print("Saindo...")
                break

            case "*":
                print("Opção inválida")


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "cliente":
        executar_cliente()
    else:
        main()