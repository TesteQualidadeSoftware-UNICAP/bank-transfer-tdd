from app.account import Account


class TransferService:
    @staticmethod
    def transfer(sender: Account, receiver: Account, amount: float):

        if amount <= 0:
            raise ValueError("Valor deve ser maior que zero")

        if sender.account_id == receiver.account_id:
            raise ValueError("Não pode transferir para a própria conta")

        sender.withdraw(amount)
        receiver.deposit(amount)

        sender.history.append(
            f"Transferência enviada: {amount} para {receiver.account_id}"
        )

        receiver.history.append(
            f"Transferência recebida: {amount} de {sender.account_id}"
        )
