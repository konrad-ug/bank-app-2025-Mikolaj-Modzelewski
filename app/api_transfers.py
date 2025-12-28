from flask import Flask, Blueprint, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

transfers = Blueprint("transfers", __name__)

@transfers.route("/api/accounts/<pesel>/transfer", methods=['PATCH'])
def transfer(pesel):
    data = request.get_json()
    print(f"Transfer request: {data}")
    result = transfers.registry.transfer_for_account(pesel, data["type"], data["amount"])
    match result:
        case 200:
            return jsonify({"message": "Transfer succesfull"}), 200
        case 400:
            return jsonify({"message": "Bad request"}), 400
        case 404:
            return jsonify({"message": "Account not found"}), 404
        case 422:
            return jsonify({"message": "Insufficient funds"}), 422