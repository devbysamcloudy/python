#Handles all the required transactions and opening of accounts
import json
import os
import sys

def create_account(id_number, name):
    account = {
        "account_no": id_number,
        "id_number":id_number,
        "name":name,
        "Transaction_history": [],
        "balance": 0
    }

    filename = f"accounts/{id_number}.json"
    with open (filename, "w") as file:
        json.dump(account,file)
    print(f"Account created successfully")

def get_account_by_id(id_number):
    filename = f"accounts/{id_number}.json"
    if not os.path.exists(filename):
        return None

    with open (filename, "r") as file:
        account = json.load(file)
        print(account)
    return account        
