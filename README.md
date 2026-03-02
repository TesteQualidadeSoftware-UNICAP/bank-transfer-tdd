# 🏦 Bank Transfer TDD

![CI](https://github.com/TesteQualidadeSoftware-UNICAP/bank-transfer-tdd/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)

Projeto acadêmico para prática de **TDD, BDD, Testes de Integração e
CI/CD** utilizando Python.

------------------------------------------------------------------------

## 📚 Objetivo

Este projeto simula um sistema bancário simples com:

-   Transferência entre contas
-   Saque
-   Testes unitários
-   Testes de integração
-   Linter (Ruff)
-   Integração contínua com GitHub Actions

O objetivo é aplicar boas práticas de Engenharia de Software.

------------------------------------------------------------------------

## 🏗 Arquitetura

Estrutura principal do projeto:

app/ - account.py - transfer_service.py - withdraw_service.py

tests/ - test_transfer_service.py - test_withdraw_service.py -
integration/ - test_bank_flow.py

------------------------------------------------------------------------

## 🧪 Tipos de Teste

### ✅ Testes Unitários

Testam classes isoladamente.

Executar: pytest -m "not integration"

------------------------------------------------------------------------

### 🔗 Testes de Integração

Testam o fluxo completo entre múltiplos componentes.

Executar: pytest -m integration

------------------------------------------------------------------------

## 🔎 Linter (Ruff)

Verificar qualidade do código:

ruff check .

Corrigir automaticamente:

ruff check . --fix

------------------------------------------------------------------------

## 🚀 CI/CD

Pipeline configurado com:

1.  Lint (Ruff)
2.  Testes Unitários
3.  Testes de Integração

O CI falha se: - O linter detectar erro - Algum teste falhar - Coverage
ficar abaixo do mínimo configurado

------------------------------------------------------------------------

## 🎯 User Stories Implementadas

### 💸 Transferência

Como cliente autenticado\
Quero transferir dinheiro\
Para enviar valores para outro usuário

### 🏦 Saque

Como cliente do banco\
Quero realizar um saque\
Para utilizar meu saldo disponível

------------------------------------------------------------------------

## 🧠 Conceitos Aplicados

-   Test-Driven Development (TDD)
-   Behavior-Driven Development (BDD)
-   Separação de responsabilidades
-   Arquitetura baseada em serviços
-   Integração contínua
-   Versionamento com Git

------------------------------------------------------------------------

## 📦 Requisitos

-   Python 3.12
-   Pytest
-   Pytest-cov
-   Pytest-bdd
-   Ruff

Instalar dependências:

pip install -r requirements.txt

------------------------------------------------------------------------

## 👩‍🏫 Contexto Acadêmico

Projeto desenvolvido para prática de:

-   Testes automatizados
-   Fluxo profissional com branches
-   Pull Requests
-   Code Review
-   Qualidade de software

------------------------------------------------------------------------

## 📄 Licença

Uso acadêmico.
