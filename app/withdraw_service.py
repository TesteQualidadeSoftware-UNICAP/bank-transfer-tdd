from app.account import Account


class WithdrawService:

    @staticmethod
    def withdraw(account: Account, amount: float):

        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        account.withdraw(amount)

        # Ajuste para evitar 150.0 no histórico
        formatted_amount = int(amount)

        account.history.append(
            f"Saque realizado: {formatted_amount}"
        )