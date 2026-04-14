# TCPServidor.py
import socket
from app.serialization.json_service import JsonService
from data.load_produtos import carregar_produtos, produtos_para_dict
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(5)

    print("\n[SERVIDOR] Rodando na porta 5000...\n")

    while True:
        conn, addr = server.accept()
        print("Cliente conectado:", addr)

        # 🔹 RECEBE E DESEMPACOTA
        dados_bytes = conn.recv(4096)
        request = JsonService.unpack(dados_bytes)

        print("Request:", request)

        # 🔹 PROCESSA
        produtos = carregar_produtos()

        # 🔹 LISTAR PRODUTOS
        if request["acao"] == "listar_produtos":
            resposta = {
                "produtos": produtos_para_dict(produtos)
            }

        # 🔹 BUSCAR PRODUTO
        elif request["acao"] == "buscar_produto":
            produto_encontrado = None

            for p in produtos:
                if p.id == request["id"]:
                    produto_encontrado = {
                        "id": p.id,
                        "nome": p.nome,
                        "preco": p.preco
                    }
                    break

            if produto_encontrado:
                resposta = {
                    "mensagem": "Produto encontrado",
                    "produto": produto_encontrado
                }
            else:
                resposta = {"erro": "Produto não encontrado"}

        # 🔹 COMPRAR PRODUTO
        elif request["acao"] == "comprar_produto":
            produto_encontrado = None

            for p in produtos:
                if p.id == request["id"]:
                    produto_encontrado = p
                    break

            if produto_encontrado:
                resposta = {
                    "mensagem": f"Compra realizada com sucesso: {produto_encontrado.nome} - R${produto_encontrado.preco:.2f}"
                }
            else:
                resposta = {"erro": "Produto não encontrado"}

        # 🔹 AÇÃO INVÁLIDA
        else:
            resposta = {"erro": "Ação inválida"}

        # 🔹 EMPACOTA E ENVIA
        resposta_bytes = JsonService.pack(resposta)
        conn.send(resposta_bytes)

        conn.close()

if __name__ == "__main__":
    main()