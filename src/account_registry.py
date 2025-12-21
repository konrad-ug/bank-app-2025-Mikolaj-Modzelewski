from src.personal_account import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        if (account.pesel != "invalid" and account.pesel != "00000000000") and any(a.pesel == account.pesel and (a.pesel != "invalid" or a.pesel != "00000000000") for a in self.accounts):
            return False
        self.accounts.append(account)
        return True
    
    def get_account_by_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return False
    
    def get_all_accounts(self):
        return self.accounts
    
    def account_count(self):
        return len(self.accounts)
    
    def update_account(self, pesel, data):
        for account in self.accounts:
            if account.pesel == pesel:
                for key in vars(account):
                    if key in data:
                        setattr(account, key, data[key])
                return True
        return False

    def delete_account(self, pesel):
        for i in range(len(self.accounts)):
            if self.accounts[i].pesel == pesel:
                self.accounts.pop(i)
                return True
        return False
