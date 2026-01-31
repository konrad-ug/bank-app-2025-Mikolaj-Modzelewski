import unittest
from unittest.mock import Mock
from src.mongo_accounts_repository import MongoAccountsRepository
from src.personal_account import PersonalAccount

class TestMongoAccountsRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MongoAccountsRepository()
        self.repo.collection = Mock()

    def test_save_all(self):
        account = PersonalAccount("Jan", "Kowalski", "12345678901")
        accounts = [account]

        self.repo.save_all(accounts)

        self.repo.collection.delete_many.assert_called_once_with({})
        self.repo.collection.update_one.assert_called()
        
        args, kwargs = self.repo.collection.update_one.call_args
        self.assertEqual(args[0], {"pesel": "12345678901"})
        self.assertEqual(args[1]["$set"]["first_name"], "Jan")

    def test_load_all(self):
        mock_document = {
            "first_name": "Anna",
            "last_name": "Nowak",
            "pesel": "98765432109",
            "balance": 100.0,
            "history": []
        }
        self.repo.collection.find.return_value = [mock_document]

        loaded_accounts = self.repo.load_all()

        self.assertEqual(len(loaded_accounts), 1)
        self.assertEqual(loaded_accounts[0].first_name, "Anna")
        self.assertEqual(loaded_accounts[0].balance, 100.0)
        self.repo.collection.find.assert_called_once()