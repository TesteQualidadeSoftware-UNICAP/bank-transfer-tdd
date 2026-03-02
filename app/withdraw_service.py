class WithdrawService:

    @staticmethod
    def withdraw(account, amount):

        # Regra 1: valor inválido
        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        # Regra 2: saldo insuficiente
        if amount > account.balance:
            raise ValueError("Saldo insuficiente")

        # Regra 3: atualizar saldo
        account.balance -= amount

        # Regra 4: registrar histórico
        account.history.append(f"Saque realizado: {amount}")