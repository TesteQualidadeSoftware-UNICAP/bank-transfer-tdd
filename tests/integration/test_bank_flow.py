import pytest

from app.account import Account
from app.transfer_service import TransferService
from app.withdraw_service import WithdrawService


@pytest.mark.integration

def test_fluxo_completo_transferencia_e_saque():
    # Given
    conta_a = Account("1", 1000)
    conta_b = Account("2", 500)

    # When
    TransferService.transfer(conta_a, conta_b, 200)
    WithdrawService.withdraw(conta_b, 100)

    # Then
    assert conta_a.balance == 800
    assert conta_b.balance == 600

    assert conta_a.history == ["Transferência enviada: 200 para 2"]

    assert conta_b.history == [
        "Transferência recebida: 200 de 1",
        "Saque realizado: 100",
    ]
