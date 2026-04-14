# produto_input_stream.py
import struct

class ProdutoInputStream:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def read(self):
        produtos = []

        while True:
            size_bytes = self.input_stream.read(4)
            if not size_bytes:
                break

            size = struct.unpack('i', size_bytes)[0]
            data = self.input_stream.read(size)

            offset = 0
            id = struct.unpack('i', data[offset:offset+4])[0]
            offset += 4

            nome_len = struct.unpack('i', data[offset:offset+4])[0]
            offset += 4

            nome = data[offset:offset+nome_len].decode()
            offset += nome_len

            preco = struct.unpack('f', data[offset:offset+4])[0]

            produtos.append((id, nome, preco))

        return produtos