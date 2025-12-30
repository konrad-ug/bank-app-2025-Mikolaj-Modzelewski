import pytest
from unittest.mock import patch
from datetime import date
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount


@pytest.mark.parametrize("account_class, account_type", [
    (lambda: PersonalAccount("John", "Doe"), "Personal"),
    (lambda: CompanyAccount("Lorem", "7342867148"), "Company"),
])

def test_send_history_via_email(account_class, account_type, mocker):
    account = account_class()
    account.history = [1, 2, 3]
    mock_send = mocker.patch("smtp.smtp.SMTPClient.send", return_value=True)
    email = "lorem@ipsum.com"
    assert account.send_history_via_email(email) is True
    mock_send.assert_called_once()
    subject, text, email_arg = mock_send.call_args[0]
    assert subject == f"Account Transfer History {date.today().strftime('%Y-%m-%d')}"
    assert text == f"{account_type} account history: {account.history}"
    assert email_arg == email

@pytest.mark.parametrize("account_class, account_type", [
    (lambda: PersonalAccount("John", "Doe"), "Personal"),
    (lambda: CompanyAccount("Lorem", "7342867148"), "Company"),
])

def test_send_history_via_email_failure(account_class, account_type, mocker):
    account = account_class()
    account.history = [1, 2, 3]
    mock_send = mocker.patch("smtp.smtp.SMTPClient.send", return_value=False)
    assert account.send_history_via_email("lorem@ipsum.com") is False
    mock_send.assert_called_once()
