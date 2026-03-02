EXERCÍCIO – BDD FORMAL (Branch: feature/bdd-exercicio)

CONTEXTO Nesta branch, você encontrará a especificação comportamental da
funcionalidade SAQUE, escrita em BDD formal utilizando Gherkin.

A especificação já foi criada, porém a implementação ainda não foi
realizada.

Seu objetivo é transformar a especificação em código executável.

------------------------------------------------------------------------

USER STORY – SAQUE

Como cliente do banco Quero realizar um saque Para utilizar meu saldo
disponível

------------------------------------------------------------------------

ESPECIFICAÇÃO COMPORTAMENTAL

Arquivo disponível: tests/features/withdraw.feature

Ele contém os seguintes cenários:

-   Saque realizado com sucesso
-   Valor inválido
-   Saldo insuficiente

ATENÇÃO: - Os cenários já estão escritos. - Os testes atualmente
falham. - A implementação ainda não existe.

------------------------------------------------------------------------

SUA MISSÃO

Você deve:

1)  Implementar os steps do BDD (@given, @when, @then)
2)  Criar o arquivo withdraw_service.py
3)  Implementar a classe WithdrawService
4)  Fazer todos os cenários passarem
5)  Garantir que o CI permaneça verde
6)  Manter cobertura mínima de 90%

------------------------------------------------------------------------

ESTRUTURA ESPERADA APÓS IMPLEMENTAÇÃO

app/ withdraw_service.py

tests/ test_withdraw_bdd.py (com steps implementados)

------------------------------------------------------------------------

FLUXO OBRIGATÓRIO

1)  Criar nova branch: git checkout -b feature/bdd-solution
2)  Implementar solução
3)  Commitar com mensagem semântica: feat: implementa saque utilizando
    BDD formal
4)  Fazer push
5)  Abrir Pull Request

------------------------------------------------------------------------

CRITÉRIOS DE AVALIAÇÃO

-   Implementação correta dos steps BDD
-   Implementação correta das regras de negócio
-   Organização do código
-   Cobertura mínima mantida
-   CI verde

------------------------------------------------------------------------

OBJETIVO PEDAGÓGICO

Este exercício tem como finalidade desenvolver:

-   Escrita e leitura de especificação comportamental
-   Ligação entre requisito e implementação
-   Uso de pytest-bdd
-   Desenvolvimento guiado por comportamento (BDD)
-   Integração contínua como validação automática

------------------------------------------------------------------------

OBSERVAÇÃO IMPORTANTE

Não altere o arquivo .feature. Ele representa o requisito formal do
sistema. A implementação deve se adaptar à especificação.
