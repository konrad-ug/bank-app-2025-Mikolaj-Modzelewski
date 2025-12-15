from src.account import PersonalAccount, CompanyAccount


class TestTransferHistory:
    def test_transaction_history_personal(self):
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(5)
        account.transfer_out(10)
        assert account.history == [5, -10]
        account.transfer_out_express(5)
        assert account.history == [5, -10, -5, -1]
    
    def test_transaction_history_company(self):
        account = CompanyAccount("Lorem", "1234567890")
        account.balance = 1000
        account.transfer_in(5)
        account.transfer_out(10)
        assert account.history == [5, -10]
        account.transfer_out_express(5)
        assert account.history == [5, -10, -5, -5]
