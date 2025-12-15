from src.account import PersonalAccount, CompanyAccount


class TestTransfers:
    def test_transfer_in_personal(self):
        account = PersonalAccount("John", "Doe", "61345678901", "PROM_123")
        account.transfer_in(-1)
        assert account.balance == 50
        account.transfer_in(1)
        assert account.balance == 51
        account.transfer_in(0)
        assert account.balance == 51

    def test_transfer_out_personal(self):
        account = PersonalAccount("John", "Doe", "61345678901", "PROM_123")
        account.transfer_out(-1)
        assert account.balance == 50
        account.transfer_out(1)
        assert account.balance == 49
        account.transfer_out(0)
        assert account.balance == 49
        account.transfer_out(50)
        assert account.balance == 49

    def test_transfer_in_company(self):
        account = CompanyAccount("Lorem", "1234567890")
        account.transfer_in(-1)
        assert account.balance == 0
        account.transfer_in(1)
        assert account.balance == 1
        account.transfer_in(0)
        assert account.balance == 1
    
    def test_transfer_out_company(self):
        account = CompanyAccount("Lorem", "1234567890")
        account.transfer_in(2)
        account.transfer_out(-1)
        assert account.balance == 2
        account.transfer_out(1)
        assert account.balance == 1
        account.transfer_out(0)
        assert account.balance == 1
        account.transfer_out(100)
        assert account.balance == 1
