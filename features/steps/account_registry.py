from behave import *
import requests

URL = "http://localhost:5000"

@step('I create an account using name: "{first_name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, first_name, last_name, pesel):
    json_body = { "name": f"{first_name}",
    "surname": f"{last_name}",
    "pesel": pesel
    }
    create_resp = requests.post(URL + "/api/accounts", json = json_body)
    assert create_resp.status_code == 201

@step('Account registry is empty')
def clear_account_registry(context):
    response = requests.get(URL + "/api/accounts")
    accounts = response.json()
    for account in accounts:
        pesel = account["pesel"]
        requests.delete(URL + f"/api/accounts/{pesel}")

@step('Number of accounts in registry equals: "{count}"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/api/accounts/count")
    assert response.status_code == 200
    assert str(response.json()["count"]) == str(count)

@step('Account with pesel "{pesel}" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@step('Account with pesel "{pesel}" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 404

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@when('I update "{field}" of account with pesel: "{pesel}" to "{value}"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid field: {field}. Must be 'name' or 'surname'.")
    mapping = {
        "name": "first_name",
        "surname": "last_name"
    }
    backend_field = mapping[field]
    json_body = { backend_field: value }
    response = requests.patch(URL + f"/api/accounts/{pesel}", json = json_body)
    assert response.status_code == 200

@then('Account with pesel "{pesel}" has "{field}" equal to "{value}"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200
    account_data = response.json()
    assert str(account_data[field]) == str(value)

@step('I make an "{type}" transfer of "{amount}" to account with pesel: "{pesel}"')
def make_transfer(context, type, amount, pesel):
    json_body = {
        "type": type,
        "amount": int(amount)
    }
    response = requests.patch(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    assert response.status_code == 200