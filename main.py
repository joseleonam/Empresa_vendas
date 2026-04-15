# main.py
import subprocess
from app.network.TCPCliente import main as cliente_main

def menu():
    print("\n=== SISTEMA DE VENDAS ===")
    print("1 - Rodar servidor TCP")
    print("2 - Rodar cliente TCP")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def rodar_servidor():
    print("Abrindo servidor em novo terminal...")
    subprocess.Popen(
        ["cmd", "/k", "python -m app.network.TCPServidor"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

def rodar_cliente():
    print("Iniciando cliente TCP...")
    cliente_main()

def main():
    while True:
        opcao = menu()
        
        if opcao == "1":
            rodar_servidor()

        elif opcao == "2":
            rodar_cliente()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()