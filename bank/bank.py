import json
import os, sys
from decorators import log
from accounts import create_account, get_account_by_id_no,update_account
from datetime import datetime

from time import sleep

@log

def new_account(trials = 0):
    if trials >= 3:
        print("Maximum trials reached")
        return None
    print("Welcome to the bank")
    print("Create account")
    id_number = input("Enter ID number:")
    account = get_account_by_id_no(id_number)
    if account:
        seconds = trials + 2
        print(f"ID number already in use. Try again in {seconds} s")
        sleep(seconds)
        new_account(trials+1)
        return
    name= input("Enter name:")
    password = input("Enter password:")
    account = create_account(name=name,password=password, id_number=id_number)

    if account:
        print(f"Welcome {account["name"]}. Account created")
    return account

@log
def deposit(account):
    transaction_history = account["Transaction_history"]
    balance = account["balance"]
    print(f"Accout balance is:{balance}")
    amount = int(input("Deposit Ammount:"))

    if amount < 0:
        print("To deposit enter ammout greater than 0")
        return None
    new_balance = balance + amount
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_history.append({"transaction_type": "Deposit", "timestamp":timestamp, "amount":amount,"balance":balance,"new_balance":new_balance})
    account['balance'] = new_balance
    account_update = update_account(account=account)
    return account_update
account = get_account_by_id_no("23454")
#print(account)
deposit(account)

def withdraw(account):
    transaction_history = account["Transaction_history"]
    balance = account["balance"]
    print(f"Accout balance is:{balance}")
    amount = int(input("Withdraw Amount:"))

    if amount < 0:
        print("To withdraw enter ammout greater than 0")
        return None
    new_balance = balance - amount
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction_history.append({"transaction_type": "Deposit", "timestamp":timestamp, "amount":amount,"balance":balance,"new_balance":new_balance})
    account['balance'] = new_balance
    account_update = update_account(account=account)
    return account_update
account = get_account_by_id_no("23454")
#print(account)
withdraw(account)