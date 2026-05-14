# app/network/cliente_rmi.py
import os
from app.proxy.vendas_proxy import VendasProxy
from app.models.cliente import Cliente
from faker import Faker

fake = Faker("pt_BR")

cliente = Cliente(
    fake.random_int(min=1, max=999),
    fake.name(),
    fake.email()
)


def menu():

    print("\n=== SISTEMA RMI DE VENDAS ===")

    print("1 - Listar produtos")
    print("2 - Buscar produto")
    print("3 - Comprar produtos")
    print("4 - Calcular total")
    print("0 - Sair")

    return input("Escolha uma opção: ")

def limpar_tela():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )

def main():

    proxy = VendasProxy()

    while True:

        opcao = menu()

        # 🔹 LISTAR PRODUTOS
        if opcao == "1":

            resultado = proxy.listar_produtos()

            limpar_tela()

            print("\n=== PRODUTOS ===")

            print(resultado)

        # 🔹 BUSCAR PRODUTO(S)
        elif opcao == "2":

            ids = input(
                "Digite os IDs separados por vírgula (ex: 1,2,3): "
            )

            lista_ids = [
                int(x.strip())
                for x in ids.split(",")
            ]

            resultado = proxy.buscar_produtos(
                lista_ids
            )

            limpar_tela()

            print("\n=== RESULTADO ===")

            print(resultado)

        # 🔹 COMPRAR PRODUTOS
        elif opcao == "3":

            ids = input(
                "Digite os IDs separados por vírgula (ex: 1,2,3): "
            )

            lista_ids = [
                int(x.strip())
                for x in ids.split(",")
            ]

            resultado = proxy.comprar_produtos(
                cliente,
                lista_ids
            )

            limpar_tela()

            print("\n=== COMPRA ===")

            print(resultado)

        # 🔹 CALCULAR TOTAL
        elif opcao == "4":

            ids = input(
                "Digite os IDs separados por vírgula (ex: 1,2,3): "
            )

            lista_ids = [
                int(x.strip())
                for x in ids.split(",")
            ]

            resultado = proxy.calcular_total(
                lista_ids
            )

            limpar_tela()

            print("\n=== TOTAL ===")

            print(resultado)

        # 🔹 SAIR
        elif opcao == "0":

            print("Encerrando cliente...")

            break

        else:

            print("Opção inválida")


if __name__ == "__main__":
    main()