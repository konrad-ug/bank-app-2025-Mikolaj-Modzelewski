from src.account import Account, Caccount


class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        account = Account("Żenia", "Brzęczyszczykiewicz")
        assert account.first_name == "Żenia"
        assert account.last_name == "Brzęczyszczykiewicz"
        assert account.balance == 0
        account = Account("ᛗᚨᚱᛁᚨᚾ", "ᚲᛟᚹᚨᛚᛊᚲᛁ")
        assert account.first_name == "ᛗᚨᚱᛁᚨᚾ"
        assert account.last_name == "ᚲᛟᚹᚨᛚᛊᚲᛁ"
        assert account.balance == 0
        account = Account("Marian", "Paździoch", "78030186911")
        assert account.pesel == "78030186911"
        account = Account("Ferdynand", "Kiepski", "77011142011")
        assert account.pesel == "77011142011"
    
    def test_pesel_length(self):
        account = Account("Lorem", "Ipsum", "dolor")
        assert account.pesel == "invalid"
        account = Account("Consectetur", "Latine", "12345678901")
        assert account.pesel == "12345678901"
    
    def test_promo_code(self):
        account = Account("Lorem", "Ipsum", "63145678901")
        assert account.balance == 0
        account = Account("Lorem", "Ipsum", "61345678901", "PROM_123")
        assert account.balance == 50
        account = Account("Lorem", "Ipsum", "63345678901", "GROM_123")
        assert account.balance == 0
        account = Account("Lorem", "Ipsum", "12345678901", "PROM_123")
        assert account.balance == 0

class TestTransfers:
    def test_transfer_in(self):
        account = Account("John", "Doe", "61345678901", "PROM_123")
        account.transfer_in(-1)
        assert account.balance == 50
        account.transfer_in(1)
        assert account.balance == 51
        account.transfer_in(0)
        assert account.balance == 51

    def test_transfer_out(self):
        account = Account("John", "Doe", "61345678901", "PROM_123")
        account.transfer_out(-1)
        assert account.balance == 50
        account.transfer_out(1)
        assert account.balance == 49
        account.transfer_out(0)
        assert account.balance == 49
        account.transfer_out(50)
        assert account.balance == 49
    
class TestCompanyAccounts:
    def test_account_creation(self):
        account = Caccount("Lorem", "1234567890")
        assert account.company_name == "Lorem"
        assert account.nip == "1234567890"
        account = Caccount("Lorem", "123456789")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
        account = Caccount("Lorem", "123456789")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
        account = Caccount("Lorem", "a234567890")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"

    def test_transfer_in(self):
        account = Account("Lorem", "1234567890")
        account.transfer_in(-1)
        assert account.balance == 0
        account.transfer_in(1)
        assert account.balance == 1
        account.transfer_in(0)
        assert account.balance == 1
    
    def test_transfer_out(self):
        account = Account("Lorem", "1234567890")
        account.transfer_in(2)
        account.transfer_out(-1)
        assert account.balance == 2
        account.transfer_out(1)
        assert account.balance == 1
        account.transfer_out(0)
        assert account.balance == 1
        account.transfer_out(100)
        assert account.balance == 1

class TestExpressTransfers:
    def test_transfer_out_express_account(self):
        account = Account("John", "Doe", "61345678901", "PROM_123")
        assert account.balance == 50
        account.transfer_out_express(-1)
        assert account.balance == 50
        account.transfer_out_express(0)
        assert account.balance == 50
        account.transfer_out_express(10)
        assert account.balance == 39
        account.transfer_out_express(100)
        assert account.balance == 39

    def test_transfer_out_express_company_account(self):
        account = Caccount("MyCompany", "1234567890")
        account.balance = 100
        account.transfer_out_express(-5)
        assert account.balance == 100
        account.transfer_out_express(0)
        assert account.balance == 100
        account.transfer_out_express(20)
        assert account.balance == 75
        account.transfer_out_express(200)
        assert account.balance == 75
