import pytest
from src.account import PersonalAccount, CompanyAccount


@pytest.mark.parametrize("account", [
    PersonalAccount("John", "Doe"),
    CompanyAccount("MyCompany", "1234567890")
])


class TestTransferHistory:
    def test_transaction_history(self, account):
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.history == [1, -1]
        account.balance = 1
        account.transfer_out_express(1)
        assert account.history in ([1, -1, -1, -1], [1, -1, -1, -5])
