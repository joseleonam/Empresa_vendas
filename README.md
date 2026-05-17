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
# Sistema Distribuído de Vendas — RMI em Python

Implementação de um sistema de vendas distribuído utilizando o conceito de Remote Method Invocation (RMI) em Python, seguindo o modelo Request-Response.

---

# Objetivo do Projeto

O objetivo deste trabalho é implementar uma aplicação distribuída utilizando o paradigma de Invocação Remota de Métodos (RMI).

O sistema permite que clientes realizem operações remotamente em um servidor de vendas através de chamadas de métodos remotos.

---



# Sistema RMI de Vendas

Projeto desenvolvido para a disciplina de Sistemas Distribuídos da Universidade Federal do Ceará (UFC - Campus Quixadá), utilizando o conceito de Remote Method Invocation (RMI) em Python.

---

# Descrição do Projeto

O projeto implementa um sistema distribuído de vendas baseado no modelo cliente-servidor utilizando o padrão Request-Response inspirado em RMI (Remote Method Invocation).

O sistema possui os seguintes métodos remotos:

1. Listar produtos
2. Buscar produtos
3. Comprar produtos
4. Calcular total da compra

A comunicação entre cliente e servidor é feita através de chamadas remotas simuladas utilizando:

- Proxy
- Dispatcher
- Request
- Response
- RemoteObjectRef

As mensagens são serializadas utilizando JSON.

---

# Estrutura do Projeto

```text
Empresa_vendas/
│
├── app/
│
│ ├── dispatcher/
│ │ └── dispatcher.py
│ │
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
│ ├── proxy/
│ │ └── vendas_proxy.py
│ │
│ ├── remote/
│ │ ├── remote_object_ref.py
│ │ ├── request.py
│ │ └── response.py
│ │
│ ├── serialization/
│ │ └── json_serializer.py
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

O projeto implementa uma simulação de RMI em Python utilizando os seguintes componentes:

## Proxy

Arquivo:

```text
app/proxy/vendas_proxy.py
```

Responsável por:

- representar o objeto remoto no cliente
- empacotar requisições
- enviar chamadas remotas
- receber respostas

---

## Dispatcher

Arquivo:

```text
app/dispatcher/dispatcher.py
```

Responsável por:

- localizar o objeto remoto
- identificar o método solicitado
- executar o método remotamente
- retornar o resultado

---

## Request

Arquivo:

```text
app/remote/request.py
```

Representa a mensagem de requisição contendo:

- referência do objeto remoto
- nome do método
- argumentos

---

## Response

Arquivo:

```text
app/remote/response.py
```

Representa a resposta enviada pelo servidor contendo:

- status da execução
- resultado do método remoto

---

## RemoteObjectRef

Arquivo:

```text
app/remote/remote_object_ref.py
```

Representa a referência remota do objeto disponibilizado pelo servidor.

---

# Representação Externa de Dados

O projeto utiliza JSON para serialização e desserialização de mensagens remotas.

Exemplo:

```python
json.dumps()
json.loads()
```

A serialização é utilizada para:

- empacotar requests
- empacotar responses
- realizar passagem por valor

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

O sistema possui os seguintes métodos remotos:

| Método | Descrição |
|---|---|
| listar_produtos() | Lista todos os produtos |
| buscar_produtos(ids) | Busca produtos por ID |
| comprar_produtos(cliente, ids) | Realiza compra |
| calcular_total(ids) | Calcula valor total |

---

# Passagem por Referência

A passagem por referência é simulada através da classe:

```python
RemoteObjectRef
```

Ela identifica o objeto remoto disponibilizado pelo servidor.

Exemplo:

```python
RemoteObjectRef("VendasService")
```

---

# Passagem por Valor

A passagem por valor é utilizada para envio de objetos locais.

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

# Requisitos Atendidos

| Requisito | Status |
|---|---|
| Comunicação cliente-servidor | ✅ |
| Arquitetura Request-Response | ✅ |
| 4 entidades | ✅ |
| 2 agregações | ✅ |
| 2 heranças | ✅ |
| 4 métodos remotos | ✅ |
| Passagem por referência | ✅ |
| Passagem por valor | ✅ |
| Serialização JSON | ✅ |

---

# Observação Importante

Python não possui uma implementação nativa equivalente ao Java RMI.

Por isso, o projeto implementa uma simulação de RMI utilizando:

- Proxy
- Dispatcher
- Request/Response
- RemoteObjectRef

seguindo os conceitos apresentados na disciplina.

---

## 🚀 Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```