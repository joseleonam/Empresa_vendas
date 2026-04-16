# mensagem_output_stream.py
import struct

class MensagemOutputStream:
    def __init__(self, mensagem, output_stream):
        self.mensagem = mensagem
        self.output_stream = output_stream

    def write(self):
        acao_bytes = self.mensagem.acao.encode()
        texto_bytes = self.mensagem.texto.encode()

        data = struct.pack('i', len(acao_bytes))
        data += acao_bytes

        # 🔥 texto
        data += struct.pack('i', len(texto_bytes))
        data += texto_bytes

        # 🔥 IDs
        data += struct.pack('i', len(self.mensagem.ids))
        for id in self.mensagem.ids:
            data += struct.pack('i', id)

        self.output_stream.write(struct.pack('i', len(data)))
        self.output_stream.write(data)
        self.output_stream.flush()