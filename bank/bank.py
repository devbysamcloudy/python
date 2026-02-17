#Handles all the required transactions and opening of accounts
import json
def create_account(id_number, name):
    account_no = "1111"
    account = {
        "account_no": account_no,
        "id_number":id_number,
        "name":name,
        "Transaction_history": [],
        "balance": 0
    }

    filename = f"{account_no}.json"
    with open (filename, "w") as file:
        json.dump(account,file)
    print(f"Account created successfully")
