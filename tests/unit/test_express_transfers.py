from src.account import PersonalAccount, CompanyAccount


class TestExpressTransfers:
    def test_transfer_out_express_personal(self):
        account = PersonalAccount("John", "Doe", "61345678901", "PROM_123")
        assert account.balance == 50
        account.transfer_out_express(-1)
        assert account.balance == 50
        account.transfer_out_express(0)
        assert account.balance == 50
        account.transfer_out_express(10)
        assert account.balance == 39
        account.transfer_out_express(100)
        assert account.balance == 39

    def test_transfer_out_express_company(self):
        account = CompanyAccount("MyCompany", "1234567890")
        account.balance = 100
        account.transfer_out_express(-5)
        assert account.balance == 100
        account.transfer_out_express(0)
        assert account.balance == 100
        account.transfer_out_express(20)
        assert account.balance == 75
        account.transfer_out_express(200)
        assert account.balance == 75
