from src.account import Account


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