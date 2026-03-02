import pytest
from app.account import Account
from app.withdraw_service import WithdrawService


def test_saque_com_sucesso():
    conta = Account("1", 500)

    WithdrawService.withdraw(conta, 200)

    assert conta.balance == 300
    assert conta.history == ["Saque realizado: 200"]


def test_nao_permite_valor_zero():
    conta = Account("1", 500)

    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta, 0)


def test_nao_permite_valor_negativo():
    conta = Account("1", 500)

    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta, -50)


def test_nao_permite_saque_sem_saldo():
    conta = Account("1", 100)

    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta, 200)