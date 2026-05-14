# app/dispatcher/dispatcher.py

from app.remote.response import Response


class Dispatcher:

    def __init__(self):
        # registro de objetos remotos disponíveis
        self.registry = {}

    def register(self, object_name, service_instance):
        """
        Registra um serviço remoto.
        """
        self.registry[object_name] = service_instance

    def dispatch(self, request):
        """
        Executa um método remoto com base na request.
        """

        try:
            # 🔹 encontra o serviço
            service = self.registry.get(
                request.object_reference.object_name
            )

            if not service:
                return Response(
                    "erro",
                    f"Serviço '{request.object_reference.object_name}' não encontrado"
                )

            # 🔹 encontra o método dinamicamente
            method = getattr(service, request.method_name, None)

            if not method:
                return Response(
                    "erro",
                    f"Método '{request.method_name}' não encontrado"
                )

            # 🔹 executa o método com argumentos
            result = method(*request.args)

            # 🔹 retorna resposta de sucesso
            return Response("ok", result)

        except Exception as e:
            return Response("erro", str(e))