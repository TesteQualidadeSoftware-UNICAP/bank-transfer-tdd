import pytest
from app.account import Account
from app.withdraw_service import WithdrawService

def test_withdrawsucess():
    conta = Account("123", 500)
    WithdrawService.withdraw(conta,100)
    assert conta.balance == 400

def test_saldosuficiente():
    conta = Account ("11", 500)
    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta,600)

def test_maiorzero():
    conta = Account ("11",500)
    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta,0)

def test_limite():
    conta = Account ("45", 3000)
    with pytest.raises(ValueError):
        WithdrawService.withdraw(conta,2001)

def test_registro():
    conta = Account("33", 500)
    WithdrawService.withdraw(conta,100)
    assert len(conta.history) == 1

