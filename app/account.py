class Account:
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
        self.history = []

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")

        self.balance -= amount
