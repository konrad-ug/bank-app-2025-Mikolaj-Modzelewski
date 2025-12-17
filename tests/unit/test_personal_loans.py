import pytest
from src.account import PersonalAccount, CompanyAccount


@pytest.fixture
def account():
    acc = PersonalAccount("John", "Doe")
    acc.balance = 1000
    return acc


class TestPersonalLoans:
    def test_last_three_deposits(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) is True
        assert account.balance == 1004

    def test_last_three_not_deposits(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.submit_for_loan(1) is False

    def test_last_not_three_deposits(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) is False

    def test_last_five_greater(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.submit_for_loan(1) is True
        assert account.balance == 1004

    def test_last_not_five_greater(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.submit_for_loan(1) is False

    def test_last_five_not_greater(self, account):
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.submit_for_loan(3) is False


