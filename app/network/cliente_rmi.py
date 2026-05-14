# app/network/cliente_rmi.py

from app.proxy.vendas_proxy import VendasProxy


def menu():

    print("\n=== SISTEMA RMI DE VENDAS ===")

    print("1 - Listar produtos")
    print("2 - Buscar produto")
    print("3 - Comprar produtos")
    print("4 - Calcular total")
    print("0 - Sair")

    return input("Escolha uma opção: ")


def main():

    proxy = VendasProxy()

    while True:

        opcao = menu()

        # 🔹 LISTAR PRODUTOS
        if opcao == "1":

            resultado = proxy.listar_produtos()

            print("\n=== PRODUTOS ===")

            print(resultado)

        # 🔹 BUSCAR PRODUTO
        elif opcao == "2":

            produto_id = int(
                input("Digite o ID do produto (ex: 1): ")
            )

            resultado = proxy.buscar_produto(
                produto_id
            )

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
                lista_ids
            )

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