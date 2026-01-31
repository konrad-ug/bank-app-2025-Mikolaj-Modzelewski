from src.personal_account import PersonalAccount

def test_to_dict():
    account = PersonalAccount("Jan", "Kowalski", "1234567890")
    
    account.balance = 150.0
    account.history = ["Deposit: 100", "Payment: 50"]

    account_dict = account.to_dict()

    expected_dict = {
        "first_name": "Jan",
        "last_name": "Kowalski",
        "pesel": "1234567890",
        "balance": 150.0,
        "history": ["Deposit: 100", "Payment: 50"]
    }

    assert account_dict == expected_dict