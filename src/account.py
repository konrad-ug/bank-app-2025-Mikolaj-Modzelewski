from smtp.smtp import SMTPClient
from datetime import date

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
    
    def send_history_via_email(self, email):
        if self.__class__.__name__ == "PersonalAccount":
            account = "Personal"
        else:
            account = "Company"
        return SMTPClient().send(f"Account Transfer History {date.today().strftime('%Y-%m-%d')}", f"{account} account history: {self.history}", email)
