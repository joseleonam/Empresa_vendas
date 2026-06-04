# SERVIDOR/main.py
import os
import subprocess
import sys


def menu():

    print("\n=== SISTEMA RMI DE VENDAS ===")

    print("1 - Rodar FastAPI")
    print("2 - Rodar Worker")
    print("0 - Sair")

    return input("Escolha uma opção: ")


def rodar_fastapi():

    print("Abrindo FastAPI em novo terminal...")

    subprocess.Popen(
        [
            "cmd",
            "/k",
            f"{sys.executable} -m FastAPI"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )


def rodar_worker():

    print("Abrindo Worker em novo terminal...")

    subprocess.Popen(
        [
            "cmd",
            "/k",
            f"{sys.executable} -m worker"
        ],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

def limpar_tela():

    os.system(
        "cls" if os.name == "nt" else "clear"
    )

def main():

    limpar_tela()

    while True:

        opcao = menu()

        # 🔹 FastAPI
        if opcao == "1":

            rodar_fastapi()

        # 🔹 Worker
        elif opcao == "2":

            rodar_worker()

        # 🔹 SAIR
        elif opcao == "0":

            print("Encerrando sistema...")

            break

        else:

            print("Opção inválida!")


if __name__ == "__main__":
    main()