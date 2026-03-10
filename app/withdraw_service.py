class WithdrawService:

    @staticmethod
    def withdraw(account, amount):
        limite = 2000

        # Regra 1: valor inválido
        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        if amount > limite:
            raise ValueError("Limite excedido")

        # Regra 2: saldo insuficiente
        if amount > account.balance:
            raise ValueError("Saldo insuficiente")

        # Regra 3: atualizar saldo
        account.balance -= amount

        # Regra 4: registrar histórico
        account.history.append(f"Saque realizado: {amount}")