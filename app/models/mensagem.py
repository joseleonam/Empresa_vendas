# mensagem.py
class Mensagem:
    def __init__(self, acao, ids=None, texto=""):
        self.acao = acao
        self.ids = ids or []
        self.texto = texto