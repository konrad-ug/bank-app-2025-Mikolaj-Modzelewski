from src.account import PersonalAccount, CompanyAccount


class TestLoans:
    def test_loans_personal(self):
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) == True
        assert account.balance == 1004
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) == False
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        assert account.submit_for_loan(1) == False
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) == False
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out_express(1)
        account.transfer_in(2)
        assert account.submit_for_loan(1) == True
        account = PersonalAccount("Lorem", "Ipsum", "12345678901")
        account.balance = 1000
        account.transfer_in(1)
        account.transfer_in(1)
        account.transfer_out_express(1)
        account.transfer_in(1)
        assert account.submit_for_loan(1) == False
