class Account:
    def __init__(self, first_name, last_name, pesel = "00000000000", code = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0 
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "invalid"
        if code[:5] == "PROM_" and len(code) == 8 and int(pesel[:2]) > 60:
            self.balance += 50

    def transfer_out(self, amount):
        if amount <= 0:
            print("Error. Number must be higher than 0. For incoming transfers please use the transfer_in() method")
        elif amount > self.balance:
            print("Error. Insufficient funds")
        else:
            self.balance -= amount

    def transfer_in(self, amount):
        if amount <= 0:
            print("Error. Number must be higher than 0. For outgoing transfers please use the transfer_out() method")
        else:
            self.balance += amount

class Caccount(Account):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        if len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = "Invalid"
        self.balance = 0