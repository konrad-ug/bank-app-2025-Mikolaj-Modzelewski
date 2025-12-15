from src.account import PersonalAccount, CompanyAccount


class TestPersonalAccount:
    def test_account_creation(self):
        account = PersonalAccount("John", "Doe")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0
        account = PersonalAccount("Żenia", "Brzęczyszczykiewicz")
        assert account.first_name == "Żenia"
        assert account.last_name == "Brzęczyszczykiewicz"
        assert account.balance == 0
        account = PersonalAccount("ᛗᚨᚱᛁᚨᚾ", "ᚲᛟᚹᚨᛚᛊᚲᛁ")
        assert account.first_name == "ᛗᚨᚱᛁᚨᚾ"
        assert account.last_name == "ᚲᛟᚹᚨᛚᛊᚲᛁ"
        assert account.balance == 0
        account = PersonalAccount("Marian", "Paździoch", "78030186911")
        assert account.pesel == "78030186911"
        account = PersonalAccount("Ferdynand", "Kiepski", "77011142011")
        assert account.pesel == "77011142011"
    
    def test_pesel_length(self):
        account = PersonalAccount("Lorem", "Ipsum", "dolor")
        assert account.pesel == "invalid"
        account = PersonalAccount("Consectetur", "Latine", "12345678901")
        assert account.pesel == "12345678901"
    
    def test_promo_code(self):
        account = PersonalAccount("Lorem", "Ipsum", "63145678901")
        assert account.balance == 0
        account = PersonalAccount("Lorem", "Ipsum", "61345678901", "PROM_123")
        assert account.balance == 50
        account = PersonalAccount("Lorem", "Ipsum", "63345678901", "GROM_123")
        assert account.balance == 0
        account = PersonalAccount("Lorem", "Ipsum", "12345678901", "PROM_123")
        assert account.balance == 0


class TestCompanyAccounts:
    def test_account_creation(self):
        account = CompanyAccount("Lorem", "1234567890")
        assert account.company_name == "Lorem"
        assert account.nip == "1234567890"
        account = CompanyAccount("Lorem", "123456789")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
        account = CompanyAccount("Lorem", "123456789")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
        account = CompanyAccount("Lorem", "a234567890")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
