from pymongo import MongoClient
from src.personal_account import PersonalAccount

class MongoAccountsRepository:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['bank_db']
        self.collection = self.db['accounts']

    def save_all(self, accounts):
        self.collection.delete_many({})
        
        for account in accounts:
            account_data = {
                "first_name": account.first_name,
                "last_name": account.last_name,
                "pesel": account.pesel,
                "balance": account.balance,
                "history": getattr(account, "history", [])
            }
            
            self.collection.update_one(
                {"pesel": account.pesel},
                {"$set": account_data},
                upsert=True
            )

    def load_all(self):
        documents = self.collection.find()
        accounts = []
        
        for doc in documents:
            account = PersonalAccount(doc["first_name"], doc["last_name"], doc["pesel"])
            
            account.balance = doc["balance"]
            if "history" in doc:
                account.history = doc["history"]
                
            accounts.append(account)
        return accounts