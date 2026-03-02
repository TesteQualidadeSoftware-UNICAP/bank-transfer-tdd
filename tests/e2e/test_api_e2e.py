import pytest
from fastapi.testclient import TestClient
from app.main import app, accounts

client = TestClient(app)


@pytest.mark.e2e
def test_fluxo_completo_via_api():

    # Limpar estado antes do teste (importante!)
    accounts.clear()

    # =========================
    # Criar contas
    # =========================
    response = client.post("/accounts/", params={
        "account_id": "1",
        "balance": 1000
    })
    assert response.status_code == 200

    response = client.post("/accounts/", params={
        "account_id": "2",
        "balance": 200
    })
    assert response.status_code == 200

    # =========================
    # Transferir dinheiro
    # =========================
    response = client.post("/transfer/", params={
        "sender_id": "1",
        "receiver_id": "2",
        "amount": 300
    })
    assert response.status_code == 200

    # =========================
    # Sacar dinheiro
    # =========================
    response = client.post("/withdraw/", params={
        "account_id": "2",
        "amount": 150
    })
    assert response.status_code == 200

    # =========================
    # Validar estado final via API
    # =========================
    response = client.get("/accounts/1")
    data = response.json()

    assert data["balance"] == 700
    assert data["history"] == [
        "Transferência enviada: 300 para 2"
    ]

    response = client.get("/accounts/2")
    data = response.json()

    assert data["balance"] == 350
    assert data["history"] == [
        "Transferência recebida: 300 de 1",
        "Saque realizado: 150"
    ]