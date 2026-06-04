# Sistema Distribuído de Vendas com Tuple Space

## Disciplina

Sistemas Distribuídos (QXD0043)

Universidade Federal do Ceará - Campus de Quixadá

Professor: Rafael Braga

## Descrição

Este projeto implementa um Sistema Distribuído de Vendas utilizando a abordagem de Comunicação Indireta baseada em Espaço de Tuplas (Tuple Space).

O objetivo é desacoplar os componentes do sistema por meio de uma memória compartilhada persistente, permitindo que produtores e consumidores troquem informações sem comunicação direta.

## Arquitetura

O sistema é composto por três componentes principais:

### Cliente

Responsável por:

* Listar produtos
* Buscar produtos
* Solicitar compras
* Calcular totais
* Consultar pedidos processados

A comunicação ocorre através da API REST.

### Servidor FastAPI

Responsável por:

* Receber requisições dos clientes
* Inserir tuplas no espaço de tuplas
* Consultar informações persistidas

### Worker

Responsável por:

* Consumir tuplas do tipo COMPRA
* Processar pedidos
* Gerar tuplas do tipo PEDIDO

## Espaço de Tuplas

Foi implementado um Tuple Space persistente utilizando SQLite.

Operações disponíveis:

* write() → insere tuplas
* read() → consulta tuplas
* take() → remove e retorna tuplas
* listar_tuplas() → exibe todas as tuplas

Exemplos:

### Produto

```python
("PRODUTO", 1, "iPhone 14", 5000)
```

### Compra

```python
(
    "COMPRA",
    {
        "id": 123,
        "nome": "João Silva",
        "email": "joao@email.com"
    },
    [1, 2]
)
```

### Pedido

```python
(
    "PEDIDO",
    {
        "Pedido_id": 10,
        "cliente_id": 123,
        "cliente_nome": "João Silva",
        "vendedor": "Maria Souza",
        "produtos": ["iPhone 14", "Galaxy S23"],
        "total": 8500
    }
)
```

## Comunicação Indireta

O cliente não conhece o Worker.

O cliente envia uma compra para o FastAPI.

O FastAPI grava a compra no Tuple Space.

O Worker consome a compra posteriormente.

Após processar, o Worker gera uma tupla de pedido.

O cliente pode recuperar seus pedidos posteriormente.

## Desacoplamento Demonstrado

### Desacoplamento Espacial

O cliente não possui qualquer referência ao Worker.

Toda comunicação ocorre através do Tuple Space.

### Desacoplamento Temporal

As compras permanecem armazenadas no SQLite.

Mesmo que o Worker esteja desligado, as compras continuam disponíveis para processamento quando ele retornar.

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLite
* Requests
* Faker
* Uvicorn

## Execução

execute criente e servidor em diretorios separados

cliente -> Empresa_vendas/Cliente/

servidor -> Empresa_vendas/Servidor/

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o FastAPI e Worker

```bash
python main.py
```

### 4. Executar o Cliente

```bash
python main.py
```
