import pytest
from app.account import Account


def test_deposito_invalido():
    conta = Account("1", 100)

    with pytest.raises(ValueError):
        conta.deposit(0)

    with pytest.raises(ValueError):
        conta.deposit(-50)