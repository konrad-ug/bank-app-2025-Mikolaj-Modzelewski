import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

@pytest.mark.parametrize("account", [
    PersonalAccount("John", "Doe"),
    CompanyAccount("MyCompany", "1234567890")
])


class TestTransfers:
    def test_transfer_in(self, account):
        with pytest.raises(ValueError):
            account.transfer_in(-1)
        with pytest.raises(ValueError):
            account.transfer_in(0)
        account.transfer_in(1)
        assert account.balance == 1

    def test_transfer_out(self, account):
        with pytest.raises(ValueError):
            account.transfer_out(-1)
        with pytest.raises(ValueError):
            account.transfer_out(0)
        with pytest.raises(RuntimeError):
            account.transfer_out(50)
        account.balance = 1
        account.transfer_out(1)
        assert account.balance == 0
