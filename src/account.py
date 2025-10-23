class Account:
    def __init__(self, first_name, last_name, pesel = "00000000000"):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "invalid"