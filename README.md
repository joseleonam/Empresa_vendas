
# 📌 Trabalho 4 – Comunicação Indireta

**Sistema de Vendas com Tuple Space (SQLite + FastAPI)**
Disciplina: Sistemas Distribuídos – QXD0043
Universidade Federal do Ceará – Campus Quixadá

---

## 🧠 1. Visão Geral

Este projeto evolui uma arquitetura de sistema distribuído previamente baseada em comunicação direta para uma arquitetura com **comunicação indireta**, utilizando o paradigma de **Espaço de Tuplas (Tuple Space)** como intermediário.

A solução foi implementada com **FastAPI** para expor serviços HTTP e um **TupleSpace persistente em SQLite** para desacoplamento entre componentes.

---

## 🏗️ 2. Arquitetura do Sistema

## 📊 Visão Lado a Lado (Cliente vs Servidor)

```text
CLIENTE                                  SERVIDOR
---------------------------------------------------------------

┌───────────────┐                       ┌─────────────────────┐
│ CLI Interface │                       │ FastAPI Server      │
└──────┬────────┘                       └─────────┬───────────┘
       │                                         │
       v                                         v
┌───────────────┐                       ┌─────────────────────┐
│ cliente_api.py│   HTTP Requests       │ ProdutosService     │
│ (requests)    │ ────────────────────> │ ComprasService      │
└──────┬────────┘                       │ FinanceiroService   │
       │                                └─────────┬───────────┘
       v                                          │
┌───────────────┐                                 │
│ Cliente Fake  │                                 │
└───────────────┘                                 v
                                        ┌─────────────────────┐
                                        │ TupleSpace (SQLite) │
                                        │ INTERMEDIÁRIO       │
                                        └─────────┬───────────┘
                                                  │
                                                  v
                                        ┌─────────────────────┐
                                        │ Worker (loop)       │
                                        │ Processa COMPRA     │
                                        └─────────────────────┘
```

---

## 🏗️ 3. Estrutura Interna (Separada)

### 👤 CLIENTE

```text
CLIENTE
┌────────────────────────────┐
│ main.py (menu CLI)         │
└────────────┬───────────────┘
             │
             v
┌────────────────────────────┐
│ cliente_api.py             │
│ - requests HTTP            │
└────────────┬───────────────┘
             │
             v
┌────────────────────────────┐
│ Geração de Cliente Fake    │
│ (Faker)                    │
└────────────────────────────┘
```

---

### 🖥️ SERVIDOR

```text
SERVIDOR
        ┌────────────────────────────┐
        │ FastAPI                    │
        └────────────┬───────────────┘
                     │
     ┌───────────────┼────────────────┐
     v               v                v
┌──────────┐ ┌──────────────┐ ┌────────────────┐
│ Produtos │ │ Compras      │ │ Financeiro     │
│ Service  │ │ Service      │ │ Service        │
└────┬─────┘ └──────┬───────┘ └──────┬─────────┘
     │              │                │
     └──────────────┼────────────────┘
                    v
        ┌────────────────────────────┐
        │ TupleSpace (SQLite)        │
        │ - write / take / read      │
        └────────────┬───────────────┘
                     │
                     v
        ┌────────────────────────────┐
        │ Worker de Processamento    │
        │ consome COMPRA             │
        └────────────────────────────┘
```

---

## ⚙️ 4. Escolha da Arquitetura

### ✔ FastAPI

Escolhi o **FastAPI** porque já estou mais familiarizado com o framework, o que facilitou o desenvolvimento, integração dos serviços e testes da API.

### ✔ Tuple Space (SQLite)

A escolha do **Tuple Space** foi feita porque:

* exige menos complexidade de implementação em comparação com Pub/Sub, filas ou multicast
* permite comunicação indireta simples
* facilita persistência dos dados

---

## 🔄 5. Comunicação Indireta

O sistema utiliza **TupleSpace como intermediário**, garantindo:

### ✔ Desacoplamento Espacial

* Cliente não conhece o consumidor final
* Comunicação ocorre via espaço compartilhado (SQLite)

### ✔ Desacoplamento Temporal

* Mensagens permanecem armazenadas no banco
* O consumidor pode estar offline no momento da escrita
* Os dados são processados posteriormente pelo worker

---

## 📄 6. Relatório Técnico

### ✔ Justificativa da Escolha

A abordagem escolhida foi o Espaço de Tuplas (Tuple Space), pois ela se adapta melhor ao cenário do sistema de vendas por permitir comunicação indireta simples e desacoplada entre cliente e servidor.

Essa escolha foi preferida em relação a alternativas como Pub-Sub, filas ou multicast porque:

* reduz a complexidade de implementação
* permite persistência natural dos dados via banco SQLite
* facilita a integração com o sistema já existente baseado em serviços

Além disso, o uso do Tuple Space se encaixa bem no modelo do projeto, pois os pedidos podem ser representados como tuplas e processados posteriormente por um worker assíncrono.

### ✔ Análise (Overhead e Desempenho)

A introdução de um intermediário (Tuple Space) traz benefícios de flexibilidade e desacoplamento, porém também gera algumas desvantagens:

📉 Overhead introduzido:

* consultas frequentes ao SQLite (I/O constante)
* polling do worker (while True + sleep)
* latência entre escrita e processamento
* aumento da complexidade de gerenciamento de estado

⚙️ Impacto no sistema:

* leve atraso no processamento de pedidos
* maior consumo de CPU pelo loop de verificação
* dependência do banco como ponto central

🛠️ Mitigação aplicada:

* uso de SQLite local para reduzir latência de rede
* estrutura simples de tuplas para reduzir parsing
* sleep controlado no worker para evitar busy waiting
* separação lógica entre serviços para reduzir carga no TupleSpace

## 🧩 Conclusão

A adoção do **Tuple Space com persistência em SQLite** permitiu a evolução do sistema para um modelo de comunicação indireta, reduzindo o acoplamento entre cliente e servidor.

Apesar de simples, a abordagem atende aos requisitos do trabalho, garantindo:

* desacoplamento espacial
* desacoplamento temporal
* comunicação assíncrona baseada em intermediário

---

Se quiser, posso agora:
✔ melhorar isso para versão “nota 10 (mais acadêmica)”
✔ ou adicionar seção de “testes de falha (servidor offline)”
✔ ou ainda deixar pronto para PDF formatado da UFC

---

## Tecnologias Utilizadas

* Python 3
* FastAPI
* SQLite
* Requests
* Faker
* Uvicorn

## 🚀 Como Executar

execute criente e servidor em diretorios separados

cliente -> Empresa_vendas/Cliente/

servidor -> Empresa_vendas/Servidor/

### 1. Criar ambiente virtual SERVIDOR

```bash
python -m venv SERVIDOR
SERVIDOR\Scripts\activate
pip install -r requirements.txt
```

execute main.py e selecione as opções FastAPI e worker

### 2. Criar ambiente virtual CLIENTE

```bash
python -m venv CLIENTE
CLIENTE\Scripts\activate
pip install -r requirements.txt
```

execute a main.py

## usar esse comando do commit pra saber quem e quando foi feita a alteração

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
