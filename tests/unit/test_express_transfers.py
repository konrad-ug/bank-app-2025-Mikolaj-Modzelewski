import pytest
from src.account import PersonalAccount, CompanyAccount

@pytest.mark.parametrize("account", [
    PersonalAccount("John", "Doe"),
    CompanyAccount("MyCompany", "1234567890")
])

class TestExpressTransfers:
    def test_transfer_out_express(self, account):
        account = PersonalAccount("John", "Doe")
        with pytest.raises(ValueError):
            account.transfer_out_express(-1)
        with pytest.raises(ValueError):
            account.transfer_out_express(0)
        with pytest.raises(RuntimeError):
            account.transfer_out_express(100)
        account.balance = 15
        account.transfer_out_express(10)
        assert account.balance in (4, 0)
        account.balance = 10
        account.transfer_out_express(10)
        assert account.balance in (-1, -5)
