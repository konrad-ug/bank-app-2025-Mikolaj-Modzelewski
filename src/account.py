class Account:
    def __init__(self):
        self.balance = 0
        self.history = []

    def transfer_out(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0. Use transfer_in() for deposits.")
        if amount > self.balance:
            raise RuntimeError("Insufficient funds for transfer.")
        self.balance -= amount
        self.history.append(-amount)

    def transfer_in(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0. Use transfer_out() for withdrawals.")
        self.balance += amount
        self.history.append(amount)
