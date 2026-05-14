# Empresa Vendas - Sistema Distribuído com RMI

Projeto desenvolvido para a disciplina de Sistemas Distribuídos utilizando Python.

O sistema implementa um modelo de comunicação distribuída baseado em Remote Method Invocation (RMI), utilizando arquitetura cliente-servidor, protocolo requisição-resposta, serialização JSON e invocação remota de métodos.

---

# Objetivos do Projeto

- Implementar comunicação distribuída utilizando RMI
- Simular chamadas remotas de métodos
- Utilizar protocolo Request/Reply
- Aplicar serialização e desserialização de dados
- Trabalhar com passagem por valor e passagem por referência
- Aplicar conceitos de Proxy e Dispatcher

---

# Tecnologias Utilizadas

- Python 3
- JSON
- Sockets TCP
- Programação Orientada a Objetos

---

# Estrutura do Projeto

```text
Empresa_vendas/
│
├── app/
│
│ ├── models/
│ │ ├── produto.py
│ │ ├── vendedor.py
│ │ ├── cliente.py
│ │ └── pedido.py
│ │
│ ├── remote/
│ │ ├── request.py
│ │ ├── response.py
│ │ └── remote_object_ref.py
│ │
│ ├── proxy/
│ │ └── vendas_proxy.py
│ │
│ ├── dispatcher/
│ │ └── dispatcher.py
│ │
│ ├── network/
│ │ ├── servidor_rmi.py
│ │ └── cliente_rmi.py
│ │
│ ├── service/
│ │ ├── vendas.py
│ │ └── vendas_service.py
│ │
│ └── serialization/
│     └── json_serializer.py
│
├── data/
│ └── load_produtos.py
│
├── main.py
│
├── requirements.txt
│
└── README.md