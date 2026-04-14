# produto_output_stream.py
import struct

class ProdutoOutputStream:
    def __init__(self, produtos, quantidade, output_stream):
        self.produtos = produtos
        self.quantidade = quantidade
        self.output_stream = output_stream

    def write(self):
        for i in range(self.quantidade):
            p = self.produtos[i]

            # Serializando atributos (id, nome, preco)
            nome_bytes = p.nome.encode()
            data = struct.pack('i', p.id)
            data += struct.pack('i', len(nome_bytes))
            data += nome_bytes
            data += struct.pack('f', p.preco)

            # envia tamanho + dados
            self.output_stream.write(struct.pack('i', len(data)))
            self.output_stream.write(data)

        self.output_stream.flush()