from src.account import Account

class PersonalAccount(Account):
    def __init__(self, first_name, last_name, pesel="00000000000", code=""):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        if len(pesel) == 11 and pesel.isdigit():
            self.pesel = pesel
        else:
            self.pesel = "invalid"

        if code[:5] == "PROM_" and len(code) == 8 and self.pesel != "invalid" and int(pesel[:2]) > 60:
            self.balance += 50
    
    def transfer_out_express(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0. Use transfer_in() for deposits.")
        if amount > self.balance:
            raise RuntimeError("Insufficient funds for express transfer.")
        self.balance -= (amount + 1)
        self.history.append(-amount)
        self.history.append(-1)

    def submit_for_loan(self, amount):
        if (len(self.history) >= 3 and all(i > 0 for i in self.history[-3:])) or (
            len(self.history) >= 5 and sum(self.history) > amount
        ):
            self.balance += amount
            return True
        return False
