from flask import Blueprint, jsonify

db_bp = Blueprint("db", __name__)

@db_bp.route("/api/accounts/save", methods=['POST'])
def save_accounts():
    current_accounts = db_bp.registry.get_all_accounts()
    
    db_bp.repo.save_all(current_accounts)
    
    return jsonify({"message": "Accounts saved successfully"}), 200

@db_bp.route("/api/accounts/load", methods=['POST'])
def load_accounts():
    db_bp.registry.accounts = [] 
    
    loaded_accounts = db_bp.repo.load_all()
    
    for account in loaded_accounts:
        db_bp.registry.add_account(account)
    
    return jsonify({"message": f"Loaded {len(loaded_accounts)} accounts"}), 200