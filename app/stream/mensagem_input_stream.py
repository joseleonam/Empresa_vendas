# mensagem_input_stream.py
import struct
from app.models.mensagem import Mensagem

class MensagemInputStream:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def read(self):
        size_bytes = self.input_stream.read(4)
        if not size_bytes:
            return None

        size = struct.unpack('i', size_bytes)[0]
        data = self.input_stream.read(size)

        offset = 0

        # 🔹 ação
        acao_len = struct.unpack('i', data[offset:offset+4])[0]
        offset += 4

        acao = data[offset:offset+acao_len].decode()
        offset += acao_len

        # 🔹 texto
        texto_len = struct.unpack('i', data[offset:offset+4])[0]
        offset += 4

        texto = data[offset:offset+texto_len].decode()
        offset += texto_len

        # 🔹 ids
        qtd_ids = struct.unpack('i', data[offset:offset+4])[0]
        offset += 4

        ids = []
        for _ in range(qtd_ids):
            id = struct.unpack('i', data[offset:offset+4])[0]
            offset += 4
            ids.append(id)

        return Mensagem(acao, ids, texto)