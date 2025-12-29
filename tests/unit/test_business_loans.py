import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

@pytest.fixture
def account():
    acc = CompanyAccount("Lorem", "7342867148")
    acc.balance = 2
    return acc

class TestBusinessLoans:
    def test_2xbalance_zus(self, account):
        account.balance += 1775
        account.transfer_out(1775)
        assert account.take_loan(1) == True
        assert account.balance == 3

    def test_2xbalance_not_zus(self, account):
        assert account.take_loan(1) == False
    
    def test_not_2xbalance_zus(self, account):
        account.balance += 1775
        account.transfer_out(1775)
        assert account.take_loan(2) == False