Feature: Transferência entre contas

  Scenario: Transferência realizada com sucesso
    Given uma conta de origem com saldo 1000
    And uma conta de destino com saldo 500
    When a transferência de 200 é realizada
    Then o saldo da conta de origem deve ser 800
    And o saldo da conta de destino deve ser 700

  Scenario: Valor inválido
    Given uma conta de origem com saldo 1000
    And uma conta de destino com saldo 500
    When a transferência de -100 é realizada
    Then uma exceção deve ser lançada