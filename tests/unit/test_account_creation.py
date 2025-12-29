import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

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
        account = PersonalAccount("John", "Doe", "78030186911")
        assert account.pesel == "78030186911"
    
    def test_pesel_length(self):
        account = PersonalAccount("John", "Doe", "Lorem")
        assert account.pesel == "invalid"
        account = PersonalAccount("John", "Doe", "12345678901")
        assert account.pesel == "12345678901"
    
    def test_promo_code(self):
        account = PersonalAccount("John", "Doe", "63145678901")
        assert account.balance == 0
        account = PersonalAccount("John", "Doe", "63345678901", "GROM_123")
        assert account.balance == 0
        account = PersonalAccount("John", "Doe", "12345678901", "PROM_123")
        assert account.balance == 0
        account = PersonalAccount("John", "Doe", "61345678901", "PROM_123")
        assert account.balance == 50


class TestCompanyAccounts:
    def test_account_creation(self):
        account = CompanyAccount("Lorem", "123456789")
        assert account.company_name == "Lorem"
        assert account.nip == "Invalid"
        account = CompanyAccount("Lorem", "a234567890")
        assert account.nip == "Invalid"
        with pytest.raises(ValueError):
            account = CompanyAccount("Lorem", "1234567890")
        account = CompanyAccount("Lorem", "7342867148")
        assert account.nip == "7342867148"
        