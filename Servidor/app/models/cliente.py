# app/models/cliente.py
class Cliente:

    def __init__(self, id, nome, email):

        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):

        return (
            f"Cliente(id={self.id}, "
            f"nome='{self.nome}', "
            f"email='{self.email}')"
        )

    def to_dict(self):

        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }