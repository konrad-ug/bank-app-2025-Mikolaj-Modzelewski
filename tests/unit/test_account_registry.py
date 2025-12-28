import pytest
from src.personal_account import PersonalAccount
from src.account_registry import AccountRegistry

@pytest.fixture
def registry():
    reg = AccountRegistry()
    return reg

class TestAccountRegistry:
    def test_registry_creation(self, registry):
        assert registry.accounts == []

    def test_account_addition(self, registry):
        account = PersonalAccount("John", "Doe", "01234567890")
        registry.add_account(account)
        assert account in registry.accounts
        result = registry.add_account(account)
        assert result == False

    def test_account_search(self, registry):
        registry.add_account(PersonalAccount("John", "Doe", "02070803628"))
        account = PersonalAccount("John", "Doe", "44051401458")
        registry.add_account(account)
        registry.add_account(PersonalAccount("John", "Doe", "99031212316"))
        assert registry.get_account_by_pesel("44051401458") == account
        assert registry.get_account_by_pesel("01234567890") == False
    
    def test_get_registry(self, registry):
        account1 = PersonalAccount("John", "Doe")
        account2 = PersonalAccount("Jane", "Doe")
        registry.add_account(account1)
        registry.add_account(account2)
        assert registry.get_all_accounts() == [account1, account2]
    
    def test_account_count(self, registry):
        account1 = PersonalAccount("John", "Doe")
        account2 = PersonalAccount("Jane", "Doe")
        registry.add_account(account1)
        registry.add_account(account2)
        assert registry.account_count() == 2

    def test_account_update(self, registry):
        account = PersonalAccount("Jane", "Doe", "99031212316")
        registry.add_account(account)
        data = {"first_name": "John", "last_name": "Xia"}
        assert registry.update_account("99031212316", data) == True
        assert registry.update_account("01234567890", data) == False
        assert registry.accounts[0].first_name == "John" and registry.accounts[0].last_name == "Xia"
    
    def test_account_deletion(self, registry):
        registry.add_account(PersonalAccount("Jane", "Doe", "99031212316"))
        assert registry.delete_account("99031212316") == True
        assert registry.accounts == []
        assert registry.delete_account("01234567890") == False
    
    def test_transfer_for_account(self, registry):
        account = PersonalAccount("John", "Doe", "01234567890")
        registry.add_account(account)
        assert registry.transfer_for_account("00000000000", "incoming", 1) == 404
        assert registry.transfer_for_account("01234567890", "incoming", -1) == 400
        assert registry.transfer_for_account("01234567890", "incoming", 100) == 200
        assert registry.transfer_for_account("01234567890", "outgoing", -1) == 400
        assert registry.transfer_for_account("01234567890", "outgoing", 101) == 422
        assert registry.transfer_for_account("01234567890", "outgoing", 50) == 200
        assert registry.transfer_for_account("01234567890", "express", -1) == 400
        assert registry.transfer_for_account("01234567890", "express", 101) == 422
        assert registry.transfer_for_account("01234567890", "express", 50) == 200

