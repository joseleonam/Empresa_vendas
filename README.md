# usar esse comando do commit pra saber quem e quando foi feita a alteração
```bash
git branch
git status
git add .
git commit -m "Jose leonam $(Get-Date)"
```
```bash
git push
```
ignora erro de commits do github
```bash
git push origin main --force
```
apaga codigo local e atualiza com o git
```bash
git fetch origin
git reset --hard origin/<nome da branch>
```
---

# Sistema Distribuído de Vendas — XML-RPC

utilizando o conceito de Remote Method Invocation (RMI) em Python através de XML-RPC.

---

# Objetivo do Projeto

O objetivo deste trabalho é implementar uma aplicação distribuída utilizando o paradigma de Invocação Remota de Métodos (RMI).

O sistema permite que clientes realizem operações remotamente em um servidor de vendas através de chamadas de métodos remotos.

---

# Descrição do Projeto

O projeto implementa um sistema distribuído de vendas baseado na arquitetura cliente-servidor utilizando XML-RPC.

O sistema possui os seguintes métodos remotos:

1. Listar produtos
2. Buscar produtos
3. Comprar produtos
4. Calcular total da compra

O cliente realiza chamadas remotas diretamente para o servidor utilizando o protocolo XML-RPC do Python.

---

# Estrutura do Projeto

```text
Empresa_vendas/
│
├── app/
│
│ ├── models/
│ │ ├── cliente.py
│ │ ├── pedido.py
│ │ ├── produto.py
│ │ └── vendedor.py
│ │
│ ├── network/
│ │ ├── cliente_rmi.py
│ │ └── servidor_rmi.py
│ │
│ └── service/
│ ├── vendas.py
│ └── vendas_service.py
│
├── data/
│ └── load_produtos.py
│
├── main.py
│
├── requirements.txt
│
└── README.md
```

---

# Conceitos de Sistemas Distribuídos Utilizados

## Comunicação Cliente-Servidor

O sistema utiliza arquitetura cliente-servidor, onde:

- O cliente realiza requisições remotas
- O servidor processa os métodos solicitados
- O servidor envia respostas ao cliente

---

# Arquitetura RMI Implementada

O projeto utiliza XML-RPC para implementar chamadas remotas de métodos em Python.

A comunicação ocorre da seguinte forma:

```text
Cliente → Chamada Remota → Servidor → Método → Resposta → Cliente
```

O XML-RPC é responsável por:

- comunicação remota
- serialização de dados
- envio de requisições
- envio de respostas
- execução remota de métodos

---

# Representação Externa de Dados

O sistema utiliza serialização automática do XML-RPC para envio de dados entre cliente e servidor.

Além disso, objetos locais são enviados por valor utilizando dicionários Python.

Exemplo:

```python
cliente.__dict__
```

O servidor reconstrói o objeto:

```python
Cliente(
    cliente_data["id"],
    cliente_data["nome"],
    cliente_data["email"]
)
```

---

# Entidades do Sistema

O sistema possui as seguintes entidades:

- Produto
- Cliente
- Vendedor
- Pedido

---

# Herança ("é-um")

O projeto implementa herança através das subclasses de Produto:

- Celular
- Capa
- Pelicula
- PowerBank

Todas herdam da classe:

```python
Produto
```

---

# Agregação ("tem-um")

O projeto implementa agregação através da classe Pedido:

- Pedido tem um Cliente
- Pedido tem um Vendedor
- Pedido tem vários Produtos

---

# Métodos Remotos Implementados

| Método | Descrição |
|---|---|
| listar_produtos() | Lista todos os produtos |
| buscar_produtos(ids) | Busca produtos por ID |
| comprar_produtos(cliente, ids) | Realiza compra |
| calcular_total(ids) | Calcula valor total |

---

# Passagem por Valor

A passagem por valor é utilizada para envio de objetos locais entre cliente e servidor.

Exemplo:

```python
cliente.__dict__
```

O servidor reconstrói o objeto recebido:

```python
Cliente(
    cliente_data["id"],
    cliente_data["nome"],
    cliente_data["email"]
)
```

---

# Requisitos Atendidos

| Requisito | Status |
|---|---|
| Comunicação cliente-servidor | ✅ |
| RMI/RPC | ✅ |
| 4 entidades | ✅ |
| 2 agregações | ✅ |
| 2 heranças | ✅ |
| 4 métodos remotos | ✅ |
| Passagem por valor | ✅ |
| XML-RPC | ✅ |
| Sem sockets manuais | ✅ |

---

# Observação Importante

Python não possui uma implementação nativa equivalente ao Java RMI.

Por isso, o projeto utiliza XML-RPC, que implementa o conceito de Remote Procedure Call (RPC), permitindo chamadas remotas de métodos entre cliente e servidor sem utilização manual de sockets.

---

## 🚀 Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```