# TCPCliente.py
import socket
from app.stream.mensagem_output_stream import MensagemOutputStream
from app.stream.mensagem_input_stream import MensagemInputStream
from app.models.mensagem import Mensagem

def menu():
    print("\n=== MENU ===")
    print("1 - Listar produtos")
    print("2 - Buscar produto por ID")
    print("3 - Comprar produto")
    print("0 - Sair")
    return input("Escolha uma opção: ")


def main():
    while True:
        opcao = menu()

        if opcao == "0":
            break

        sock = socket.socket()
        sock.connect(("localhost", 5000))

        # 🔥 usamos Produto como "mensagem"
        if opcao == "1":
            msg = Mensagem("LISTAR")

        elif opcao == "2":
            ids = input("IDs (ex: 1,2,3): ")
            lista_ids = [int(x.strip()) for x in ids.split(",")]
            msg = Mensagem("BUSCAR", lista_ids)

        elif opcao == "3":
            ids = input("IDs (ex: 1,2,3): ")
            lista_ids = [int(x.strip()) for x in ids.split(",")]
            msg = Mensagem("COMPRAR", lista_ids)

        else:
            print("Opção inválida")
            continue

        # 🔹 envia via stream
        writer = MensagemOutputStream(msg, sock.makefile("wb"))
        writer.write()

        # 🔹 recebe resposta via stream
        reader = MensagemInputStream(sock.makefile("rb"))
        resposta = reader.read()

        print("\n📦 Resposta do servidor:")
        print(resposta.texto)

        sock.close()


if __name__ == "__main__":
    main()