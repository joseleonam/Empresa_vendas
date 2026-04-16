# TCPServidor.py
import socket
from app.stream.mensagem_input_stream import MensagemInputStream
from app.stream.mensagem_output_stream import MensagemOutputStream
from data.load_produtos import carregar_produtos
from app.models.vendedor import Vendedor
from app.service.vendas_service import VendasService
from app.models.mensagem import Mensagem
from faker import Faker

fake = Faker("pt_BR")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(5)

    print("\n[SERVIDOR] Rodando na porta 5000...\n")

    while True:
        conn, addr = server.accept()
        print("Cliente conectado:", addr)

        reader = MensagemInputStream(conn.makefile("rb"))
        msg = reader.read()

        if not msg:
            conn.close()
            continue

        produtos = carregar_produtos()

        # 🔹 LISTAR
        if msg.acao == "LISTAR":
            texto = "\n".join(
                f"{p.id} - {p.nome} - R${p.preco:.2f}"
                for p in produtos
            )

        # 🔹 BUSCAR
        elif msg.acao == "BUSCAR":
            encontrados = [p for p in produtos if p.id in msg.ids]

            if encontrados:
                texto = "\n".join(
                    f"{p.id} - {p.nome} - R${p.preco:.2f}"
                    for p in encontrados
                )
            else:
                texto = "Nenhum produto encontrado"

        # 🔹 COMPRAR
        elif msg.acao == "COMPRAR":
            encontrados = [p for p in produtos if p.id in msg.ids]

            if encontrados:
                vendedor = Vendedor(fake.name())
                service = VendasService(vendedor)
                texto = service.vender(encontrados)  # usa sua mensagem
                
            else:
                texto = "Nenhum produto encontrado para compra"

        else:
            texto = "Ação inválida"

        # 🔹 resposta como mensagem
        resposta = Mensagem("RESPOSTA", [], texto)

        writer = MensagemOutputStream(resposta, conn.makefile("wb"))
        writer.write()

        conn.close()


if __name__ == "__main__":
    main()