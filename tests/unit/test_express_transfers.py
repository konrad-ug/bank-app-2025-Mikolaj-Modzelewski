import pytest
from src.account import PersonalAccount, CompanyAccount

class TestExpressTransfers:
    def test_transfer_out_express_personal(self):
        account = PersonalAccount("John", "Doe")
        with pytest.raises(ValueError):
            account.transfer_out_express(-1)
        with pytest.raises(ValueError):
            account.transfer_out_express(0)
        with pytest.raises(RuntimeError):
            account.transfer_out_express(100)
        account.balance = 11
        account.transfer_out_express(10)
        assert account.balance == 0
        account.balance = 10
        account.transfer_out_express(10)
        assert account.balance == -1

    def test_transfer_out_express_company(self):
        account = CompanyAccount("MyCompany", "1234567890")
        with pytest.raises(ValueError):
            account.transfer_out_express(-1)
        with pytest.raises(ValueError):
            account.transfer_out_express(0)
        with pytest.raises(RuntimeError):
            account.transfer_out_express(100)
        account.balance = 15
        account.transfer_out_express(10)
        assert account.balance == 0
        account.balance = 10
        account.transfer_out_express(10)
        assert account.balance == -5
