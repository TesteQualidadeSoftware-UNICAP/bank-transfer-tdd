from fastapi import FastAPI, HTTPException
from app.account import Account
from app.transfer_service import TransferService
from app.withdraw_service import WithdrawService

app = FastAPI(title="Bank Transfer API")

# Simulação de banco em memória
accounts: dict[str, Account] = {}


# =========================
# ROOT
# =========================
@app.get("/")
def home():
    return {"message": "Bank Transfer API is running"}


# =========================
# CREATE ACCOUNT
# =========================
@app.post("/accounts/")
def create_account(account_id: str, balance: float):

    if account_id in accounts:
        raise HTTPException(status_code=400, detail="Conta já existe")

    if balance < 0:
        raise HTTPException(status_code=400, detail="Saldo inicial inválido")

    accounts[account_id] = Account(account_id, balance)

    return {"message": "Conta criada com sucesso"}


# =========================
# GET ACCOUNT
# =========================
@app.get("/accounts/{account_id}")
def get_account(account_id: str):

    account = accounts.get(account_id)

    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    return {
        "account_id": account.account_id,
        "balance": account.balance,
        "history": account.history
    }


# =========================
# TRANSFER
# =========================
@app.post("/transfer/")
def transfer(sender_id: str, receiver_id: str, amount: float):

    sender = accounts.get(sender_id)
    receiver = accounts.get(receiver_id)

    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    try:
        TransferService.transfer(sender, receiver, amount)
        return {"message": "Transferência realizada com sucesso"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# =========================
# WITHDRAW
# =========================
@app.post("/withdraw/")
def withdraw(account_id: str, amount: float):

    account = accounts.get(account_id)

    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    try:
        WithdrawService.withdraw(account, amount)
        return {"message": "Saque realizado com sucesso"}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))