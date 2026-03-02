# 🏦 Bank Transfer TDD
![CI](https://github.com/TesteQualidadeSoftware-UNICAP/bank-transfer-tdd/actions/workflows/ci.yml/badge.svg)

Projeto educacional com padrão de mercado para simular evolução de um
sistema bancário utilizando:

-   Python 3.12
-   Pytest
-   Cobertura de código (pytest-cov)
-   Integração Contínua (GitHub Actions)
-   Fluxo com Branch + Pull Request

------------------------------------------------------------------------

# 📖 Contexto

Você faz parte de um time que mantém um sistema bancário simplificado.

Atualmente o sistema já possui:

-   Transferência entre contas
-   Testes automatizados
-   Cobertura mínima obrigatória
-   CI configurada

Sua missão é evoluir o sistema implementando uma nova funcionalidade
seguindo boas práticas profissionais.

------------------------------------------------------------------------

# 💸 Funcionalidade Já Implementada

## Transferência entre contas

Regras implementadas:

-   O valor deve ser maior que zero
-   Não pode transferir para a própria conta
-   Deve haver saldo suficiente
-   Deve atualizar o saldo corretamente
-   Deve registrar histórico da operação

------------------------------------------------------------------------

# 🎯 Nova User Story -- Saque

> Como cliente do banco\
> Quero realizar um saque\
> Para utilizar meu saldo disponível

------------------------------------------------------------------------

# ✅ Critérios de Aceite (BDD -- Given / When / Then)

## 🟢 Cenário 1 -- Saque realizado com sucesso

**Given** que o cliente possui saldo suficiente na conta\
**When** ele solicitar um saque com valor maior que zero e dentro do
limite disponível\
**Then** o saldo da conta deve ser reduzido corretamente\
**And** a operação deve ser registrada no histórico

------------------------------------------------------------------------

## 🔴 Cenário 2 -- Valor inválido (zero ou negativo)

**Given** que o cliente possui saldo na conta\
**When** ele solicitar um saque com valor menor ou igual a zero\
**Then** o sistema deve lançar uma exceção\
**And** o saldo da conta não deve ser alterado\
**And** nenhuma operação deve ser registrada no histórico

------------------------------------------------------------------------

## 🔴 Cenário 3 -- Saldo insuficiente

**Given** que o cliente possui saldo menor que o valor solicitado\
**When** ele tentar realizar o saque\
**Then** o sistema deve lançar uma exceção\
**And** o saldo da conta não deve ser alterado\
**And** nenhuma operação deve ser registrada no histórico

------------------------------------------------------------------------

# 🧪 Requisitos Técnicos

Você deve:

-   Criar o arquivo `withdraw_service.py`
-   Implementar a classe `WithdrawService`
-   Criar os testes unitários antes da implementação (TDD)
-   Garantir que todos os testes passem
-   Manter cobertura mínima de **90%**
-   Garantir que o CI fique verde
-   Não alterar os testes existentes da funcionalidade de transferência

------------------------------------------------------------------------

# 🔁 Fluxo Obrigatório (Simulação de Mercado)

1.  Criar uma nova branch:

``` bash
git checkout -b feature/withdraw
```

2.  Implementar a solução

3.  Fazer commit com mensagem semântica:

``` bash
git commit -m "feat: implementa serviço de saque"
```

4.  Enviar para o repositório remoto:

``` bash
git push origin feature/withdraw
```

5.  Abrir Pull Request

6.  Aguardar validação automática do CI

⚠️ Pull Request com CI falhando não será aceito.

------------------------------------------------------------------------

# 📂 Estrutura do Projeto

    app/
      account.py
      transfer_service.py
      withdraw_service.py (a ser criado)

    tests/
      test_transfer_service.py
      test_withdraw_service.py (a ser criado)

------------------------------------------------------------------------

# 🚀 Como Executar Localmente

Instalar dependências:

``` bash
pip install -r requirements.txt
```

Rodar testes:

``` bash
pytest
```

Rodar testes com cobertura:

``` bash
pytest --cov=app --cov-report=term-missing
```

Gerar relatório HTML:

``` bash
pytest --cov=app --cov-report=html
```

Abrir:

    htmlcov/index.html

------------------------------------------------------------------------

# 🤖 Integração Contínua (CI)

O projeto possui pipeline configurado no GitHub Actions.

O CI:

-   Executa automaticamente em push e pull request
-   Roda todos os testes
-   Verifica cobertura mínima de 90%
-   Falha se algum teste falhar
-   Falha se cobertura for inferior ao mínimo exigido

------------------------------------------------------------------------

# 📊 Critérios de Avaliação

  Critério                           Pontuação
  ---------------------------------- -----------
  Testes corretos e completos        2.0
  Implementação correta das regras   2.0
  Aplicação de TDD                   1.0
  Organização e clareza do código    1.0
  Cobertura mínima e CI verde        2.0
  Uso correto de branch e commits    2.0

**Total: 10 pontos**

------------------------------------------------------------------------

# 🚀 Desafio (Opcional -- Diferencial)

Refatore o código para evitar duplicação entre:

-   `TransferService`
-   `WithdrawService`

Sugestões:

-   Avaliar extração de regras comuns
-   Melhorar organização da camada de serviços
-   Aplicar princípio da responsabilidade única (SRP)

------------------------------------------------------------------------

# 🧠 Objetivo da Atividade

Esta atividade simula um ambiente real de desenvolvimento profissional:

-   Evolução incremental do sistema
-   Testes automatizados como garantia de qualidade
-   Integração contínua
-   Uso de branches e Pull Requests
-   Validação automática de cobertura