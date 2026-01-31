import pytest
from unittest.mock import Mock
from src.mongo_accounts_repository import MongoAccountsRepository
from src.personal_account import PersonalAccount

@pytest.fixture
def repo():
    repository = MongoAccountsRepository()
    repository.collection = Mock()
    return repository

def test_save_all(repo):
    account = PersonalAccount("Jan", "Kowalski", "12345678901")
    accounts = [account]
    repo.save_all(accounts)
    repo.collection.delete_many.assert_called_once_with({})
    repo.collection.update_one.assert_called()
    args, kwargs = repo.collection.update_one.call_args

    assert args[0] == {"pesel": "12345678901"}
    assert args[1]["$set"]["first_name"] == "Jan"

def test_load_all(repo):
    mock_document = {
        "first_name": "Anna",
        "last_name": "Nowak",
        "pesel": "98765432109",
        "balance": 100.0,
        "history": []
    }
    repo.collection.find.return_value = [mock_document]
    loaded_accounts = repo.load_all()

    assert len(loaded_accounts) == 1
    assert loaded_accounts[0].first_name == "Anna"
    assert loaded_accounts[0].balance == 100.0
    repo.collection.find.assert_called_once()