# main.py
import subprocess
import sys


def menu():

    print("\n=== SISTEMA RMI DE VENDAS ===")

    print("1 - Rodar servidor RMI")
    print("2 - Rodar cliente RMI")
    print("0 - Sair")

    return input("Escolha uma opção: ")


def rodar_servidor():

    print("Abrindo servidor RMI em novo terminal...")

    subprocess.Popen(
        [
            "cmd",
            "/k",
            f"{sys.executable} -m app.network.servidor_rmi"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


def rodar_cliente():

    print("Abrindo cliente RMI em novo terminal...")

    subprocess.Popen(
        [
            "cmd",
            "/k",
            f"{sys.executable} -m app.network.cliente_rmi"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


def main():

    while True:

        opcao = menu()

        # 🔹 SERVIDOR
        if opcao == "1":

            rodar_servidor()

        # 🔹 CLIENTE
        elif opcao == "2":

            rodar_cliente()

        # 🔹 SAIR
        elif opcao == "0":

            print("Encerrando sistema...")

            break

        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()