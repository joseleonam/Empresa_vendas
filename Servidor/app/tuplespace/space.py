#
import os
import sqlite3
import json


class TupleSpace:

    def __init__(self, db_name="data/tuplespace.db"):

         # 🔥 garante que a pasta existe
        os.makedirs(os.path.dirname(db_name), exist_ok=True)

        self.conn = sqlite3.connect(
            db_name,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tuplas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                dados TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def write(self, tupla):

        tipo = tupla[0]

        dados = json.dumps(
            list(tupla[1:]),
            ensure_ascii=False
        )

        self.cursor.execute(
            """
            INSERT INTO tuplas(tipo, dados)
            VALUES (?, ?)
            """,
            (tipo, dados)
        )

        self.conn.commit()

    def read(self, tipo):

        self.cursor.execute(
            """
            SELECT id, dados
            FROM tuplas
            WHERE tipo = ?
            ORDER BY id
            LIMIT 1
            """,
            (tipo,)
        )

        resultado = self.cursor.fetchone()

        if not resultado:
            return None

        _, dados = resultado

        return (
            tipo,
            *json.loads(dados)
        )

    def take(self, tipo):

        self.cursor.execute(
            """
            SELECT id, dados
            FROM tuplas
            WHERE tipo = ?
            ORDER BY id
            LIMIT 1
            """,
            (tipo,)
        )

        resultado = self.cursor.fetchone()

        if not resultado:
            return None

        id_tupla, dados = resultado

        self.cursor.execute(
            """
            DELETE FROM tuplas
            WHERE id = ?
            """,
            (id_tupla,)
        )

        self.conn.commit()

        return (
            tipo,
            *json.loads(dados)
        )

    def listar_tuplas(self):

        self.cursor.execute(
            """
            SELECT tipo, dados
            FROM tuplas
            ORDER BY id
            """
        )

        resultados = self.cursor.fetchall()

        return [
            (
                tipo,
                *json.loads(dados)
            )
            for tipo, dados in resultados
        ]
    
    def take_pedido_cliente(self, cliente_id):

        self.cursor.execute(
            """
            SELECT id, dados
            FROM tuplas
            WHERE tipo='PEDIDO'
            ORDER BY id
            """
        )

        resultados = self.cursor.fetchall()

        for id_tupla, dados in resultados:

            pedido = json.loads(dados)[0]

            if pedido["cliente_id"] == cliente_id:

                self.cursor.execute(
                    """
                    DELETE FROM tuplas
                    WHERE id=?
                    """,
                    (id_tupla,)
                )

                self.conn.commit()

                return pedido

        return None