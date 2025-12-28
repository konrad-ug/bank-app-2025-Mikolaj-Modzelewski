from flask import Flask, Blueprint, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

crud = Blueprint("crud", __name__)

@crud.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"], data.get("code", ""))
    if crud.registry.add_account(account) == False:
        return jsonify({"message": "Account with this PESEL already exists"}), 409
    return jsonify({"message": "Account created"}), 201

@crud.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = crud.registry.get_all_accounts()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":
    acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@crud.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = crud.registry.account_count()
    return jsonify({"count": count}), 200

@crud.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    print("Get account request received")
    account = crud.registry.get_account_by_pesel(pesel)
    if not account:
        return jsonify({"message": "Account not found"}), 404
    return jsonify({"name": account.first_name, "surname": account.last_name, "pesel": account.pesel, "balance": account.balance}), 200

@crud.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    data = request.get_json()
    print(f"Update account request: {data}")
    if crud.registry.update_account(pesel, data) == True:
        return jsonify({"message": "Account updated"}), 200
    return jsonify({"message": "Account not found"}), 404

@crud.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    print(f"Delete account request received")
    if crud.registry.delete_account(pesel) == True:
        return jsonify({"message": "Account deleted"}), 200
    return jsonify({"message": "Account not found"}), 404
