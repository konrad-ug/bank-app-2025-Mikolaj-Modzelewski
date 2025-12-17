from src.account import PersonalAccount

class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account: PersonalAccount):
        self.accounts.append(account)
    
    def search_account(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
    
    def get_registry(self):
        return self.accounts
    
    def account_count(self):
        return len(self.accounts)