import pytest
from src.account import PersonalAccount
from src.account_registry import AccountRegistry

@pytest.fixture
def registry():
    reg = AccountRegistry()
    return reg

class TestAccountRegistry:
    def test_account_creation(self, registry):
        assert registry.accounts == []

    def test_account_addition(self, registry):
        account = PersonalAccount("John", "Doe")
        registry.add_account(account)
        assert account in registry.accounts
    
    def test_account_search(self, registry):
        registry.add_account(PersonalAccount("John", "Doe", "02070803628"))
        account = PersonalAccount("John", "Doe", "44051401458")
        registry.add_account(account)
        registry.add_account(PersonalAccount("John", "Doe", "99031212316"))
        assert registry.search_account("44051401458") == account
    
    def test_get_registry(self, registry):
        account1 = PersonalAccount("John", "Doe")
        account2 = PersonalAccount("Jane", "Doe")
        registry.add_account(account1)
        registry.add_account(account2)
        assert registry.get_registry() == [account1, account2]
    
    def test_account_count(self, registry):
        account1 = PersonalAccount("John", "Doe")
        account2 = PersonalAccount("Jane", "Doe")
        registry.add_account(account1)
        registry.add_account(account2)
        assert registry.account_count() == 2
