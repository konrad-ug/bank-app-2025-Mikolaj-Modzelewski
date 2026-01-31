from flask import Flask
from app.api_CRUD import crud
from app.api_transfers import transfers
from app.api_db import db_bp
from src.account_registry import AccountRegistry
from src.mongo_accounts_repository import MongoAccountsRepository

app = Flask(__name__)
registry = AccountRegistry()
repo = MongoAccountsRepository()

crud.registry = registry
transfers.registry = registry

db_bp.registry = registry
db_bp.repo = repo

app.register_blueprint(crud)
app.register_blueprint(transfers)
app.register_blueprint(db_bp)

if __name__ == "__main__": # pragma: no cover
    app.run(debug = True)
