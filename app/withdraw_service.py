from app.account import Account


class WithdrawService:
    @staticmethod
    def withdraw(account: Account, amount: float):

        # Regra 1: valor deve ser maior que zero
        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        # Regra 2: delega validação de saldo à entidade
        account.withdraw(amount)

        # Regra 3: registrar histórico
        account.history.append(f"Saque realizado: {amount}")
