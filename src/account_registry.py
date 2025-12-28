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

    def transfer_for_account(self, pesel, transaction_type, amount):
        account = self.get_account_by_pesel(pesel)
        if account == False:
            return 404
        match transaction_type:
            case "incoming":
                try:
                    account.transfer_in(amount)
                except ValueError:
                    return 400
            case "outgoing":
                try:
                    account.transfer_out(amount)
                except ValueError:
                    return 400
                except RuntimeError:
                    return 422
            case "express":
                try:
                    account.transfer_out_express(amount)
                except ValueError:
                    return 400
                except RuntimeError:
                    return 422
            case _:
                return 400
        return 200