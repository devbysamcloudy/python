#Handle account logics 
#Handles all the required transactions and opening of accounts
import json
import os
import sys
from decorators import log
@log
def get_account_by_id_no(id_number):
    filename = f"accounts/{id_number}.json"
    print(filename)

    if not os.path.exists(filename):
        print("Account with ID number {id_number} does not exist")
        return None
    with open(filename,"r") as file:
        account = json.load(file)
    print(account)
    return account
@log
def update_account(account):
    id_number = account["id_number"]
    filename =f"accounts/{id_number}.json"

    if not os.path.exists(filename):
        return None
    with open(filename, "w") as file:
        json.dump(account,file)
        return True

@log
def create_account(id_number, name, password):
    account_no = "1111"
    if  get_account_by_id(account_no):
        print("Account already exists")
        return None
    

    account = {
        "account_no": id_number,
        "id_number":id_number,
        "name":name,
        "Transaction_history": [],
        "balance": 0,
        "password": password
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

   


