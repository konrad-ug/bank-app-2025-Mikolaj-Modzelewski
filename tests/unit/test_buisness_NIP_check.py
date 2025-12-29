import pytest
from src.company_account import CompanyAccount

@pytest.mark.parametrize(
    "NIP, isvalid",
    [
        ("7342867148", True),
        ("9571014371", False),
    ]
)

class TestCompanyNIPCheck:
    def test_check_NIP(self, NIP, isvalid):
        account = CompanyAccount("CD Projekt S.A.", NIP)
        assert account.check_NIP() == isvalid