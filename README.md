# 🏦 Bank Transfer API

![CI](https://github.com/SEU_USUARIO/SEU_REPO/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)

Projeto acadêmico demonstrando **TDD, Integração, E2E, API REST e
CI/CD** utilizando Python e FastAPI.

------------------------------------------------------------------------

## 📚 Objetivo

Este projeto simula um sistema bancário com:

-   Criação de contas
-   Transferência entre contas
-   Saque
-   API REST com FastAPI
-   Testes Unitários
-   Testes End-to-End (E2E) via HTTP
-   Linter (Ruff)
-   Coverage mínimo obrigatório
-   Integração Contínua (GitHub Actions)

------------------------------------------------------------------------

## 🏗 Arquitetura

Estrutura principal:

app/ - account.py - transfer_service.py - withdraw_service.py - main.py

tests/ - test_transfer_service.py - e2e/ - test_api_e2e.py

------------------------------------------------------------------------

## 🌐 Executando a API

Instalar dependências:

pip install -r requirements.txt

Executar servidor:

uvicorn app.main:app --reload

Acessar documentação automática:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🧪 Testes

### ✅ Testes Unitários

pytest -m "not e2e"

### 🌐 Testes E2E (via API)

pytest -m e2e

### 🚀 Executar todos os testes

pytest

------------------------------------------------------------------------

## 📊 Coverage

Cobertura mínima configurada no CI:

--cov-fail-under=90

Executar localmente:

pytest --cov=app --cov-report=term-missing

------------------------------------------------------------------------

## 🔎 Lint

Verificar qualidade do código:

ruff check .

Corrigir automaticamente:

ruff check . --fix

------------------------------------------------------------------------

## 🔁 CI/CD

Pipeline configurada com:

1.  Lint (Ruff)
2.  Testes Unitários + Coverage
3.  Testes E2E

A pipeline falha se:

-   Algum teste falhar
-   Coverage ficar abaixo de 90%
-   O linter detectar problemas

------------------------------------------------------------------------

## 🧠 Conceitos Aplicados

-   Test-Driven Development (TDD)
-   Testes de Integração
-   Testes End-to-End (E2E)
-   API REST com FastAPI
-   Separação de responsabilidades
-   Arquitetura em camadas
-   Integração Contínua (CI)
-   Qualidade de código automatizada

------------------------------------------------------------------------

## 📦 Requisitos

-   Python 3.12
-   FastAPI
-   Uvicorn
-   Pytest
-   Pytest-cov
-   Ruff

Instalar dependências:

pip install -r requirements.txt

------------------------------------------------------------------------

## 👩‍🏫 Contexto Acadêmico

Projeto utilizado para ensino de:

-   Engenharia de Software
-   Testes automatizados
-   Versionamento com Git
-   Boas práticas de desenvolvimento
-   CI/CD

------------------------------------------------------------------------

## 📄 Licença

Uso acadêmico.
