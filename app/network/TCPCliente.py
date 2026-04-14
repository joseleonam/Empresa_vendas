# TCPCliente.py
import socket
from app.serialization.json_service import JsonService


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
            print("Saindo...")
            break

        # 🔹 cria conexão
        sock = socket.socket()
        sock.connect(("localhost", 5000))

        # 🔹 monta request
        if opcao == "1":
            request = {
                "acao": "listar_produtos"
            }

        elif opcao == "2":
            id_produto = input("Digite o ID do produto: ")
            request = {
                "acao": "buscar_produto",
                "id": int(id_produto)
            }

        elif opcao == "3":
            id_produto = input("Digite o ID do produto: ")
            request = {
                "acao": "comprar_produto",
                "id": int(id_produto)
            }

        else:
            print("Opção inválida!")
            sock.close()
            continue

        # 🔹 envia (empacota)
        dados = JsonService.pack(request)
        sock.send(dados)

        # 🔹 recebe resposta
        resposta_bytes = sock.recv(4096)
        resposta = JsonService.unpack(resposta_bytes)

        # 🔹 trata resposta

        if "produtos" in resposta:
            for p in resposta["produtos"]:
                print(f"{p.get('id','?')} - {p['nome']} - R${p['preco']}")

        if "mensagem" in resposta:
            print(resposta["mensagem"])

        if "produto" in resposta:
            p = resposta["produto"]
            print(f"{p.get('id','?')} - {p['nome']} - R${p['preco']}")

        if "erro" in resposta:
            print("Erro:", resposta["erro"])



        sock.close()


if __name__ == "__main__":
    main()