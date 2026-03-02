import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from app.account import Account
from app.transfer_service import TransferService

# Carrega automaticamente todos os cenários do arquivo
scenarios("features/transfer.feature")


@given(parsers.parse("uma conta de origem com saldo {saldo:d}"), target_fixture="conta_origem")
def conta_origem(saldo):
    return Account("1", saldo)


@given(parsers.parse("uma conta de destino com saldo {saldo:d}"), target_fixture="conta_destino")
def conta_destino(saldo):
    return Account("2", saldo)


@when(parsers.parse("a transferência de {valor:d} é realizada"), target_fixture="resultado")
def realizar_transferencia(conta_origem, conta_destino, valor):
    try:
        TransferService.transfer(conta_origem, conta_destino, valor)
        return None
    except Exception as e:
        return e


@then(parsers.parse("o saldo da conta de origem deve ser {saldo:d}"))
def verificar_saldo_origem(conta_origem, saldo):
    assert conta_origem.balance == saldo


@then(parsers.parse("o saldo da conta de destino deve ser {saldo:d}"))
def verificar_saldo_destino(conta_destino, saldo):
    assert conta_destino.balance == saldo


@then("uma exceção deve ser lançada")
def verificar_excecao(resultado):
    assert isinstance(resultado, Exception)