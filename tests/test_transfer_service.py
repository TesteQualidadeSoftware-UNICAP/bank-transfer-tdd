import pytest
from app.account import Account
from app.transfer_service import TransferService


def test_transferencia_com_sucesso():
    sender = Account("1", 1000)
    receiver = Account("2", 500)

    TransferService.transfer(sender, receiver, 200)

    assert sender.balance == 800
    assert receiver.balance == 700
    assert len(sender.history) == 1
    assert len(receiver.history) == 1


def test_nao_permite_valor_negativo():
    sender = Account("1", 1000)
    receiver = Account("2", 500)

    with pytest.raises(ValueError):
        TransferService.transfer(sender, receiver, -100)


def test_nao_permite_transferir_para_mesma_conta():
    account = Account("1", 1000)

    with pytest.raises(ValueError):
        TransferService.transfer(account, account, 100)


def test_nao_permite_transferencia_sem_saldo():
    sender = Account("1", 100)
    receiver = Account("2", 500)

    with pytest.raises(ValueError):
        TransferService.transfer(sender, receiver, 200)