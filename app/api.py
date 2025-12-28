from flask import Flask
from app.api_CRUD import crud
from app.api_transfers import transfers
from src.account_registry import AccountRegistry

app = Flask(__name__)
registry = AccountRegistry()

crud.registry = registry
transfers.registry = registry

app.register_blueprint(crud)
app.register_blueprint(transfers)

if __name__ == "__main__":
    app.run(debug = True)
