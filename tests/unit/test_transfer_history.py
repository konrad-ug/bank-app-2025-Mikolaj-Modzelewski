import pytest
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

@pytest.mark.parametrize("account", [
    lambda: PersonalAccount("John", "Doe"),
    lambda: CompanyAccount("Lorem", "7342867148")
])

class TestTransferHistory:
    def test_transaction_history(self, account):
        account = account()
        account.transfer_in(1)
        account.transfer_out(1)
        account.balance = 1
        account.transfer_out_express(1)
        assert account.history in ([1, -1, -1, -1], [1, -1, -1, -5])
