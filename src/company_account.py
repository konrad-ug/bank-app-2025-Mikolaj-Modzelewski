from src.account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__()
        self.company_name = company_name
        if len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = "Invalid"

    def transfer_out_express(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0. Use transfer_in() for deposits.")
        if amount > self.balance:
            raise RuntimeError("Insufficient funds for express transfer.")
        self.balance -= (amount + 5)
        self.history.append(-amount)
        self.history.append(-5)

    def take_loan(self, amount):
        if amount <= (self.balance / 2) and -1775 in self.history:
            self.balance += amount
            return True
        return False
