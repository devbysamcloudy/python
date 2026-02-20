#User interface handling
"""
Contains the main logics 

"""

from auth import login
from bank import withdraw, deposit, new_account
from time import sleep

def main():
    print("Welcome to soft bank")
    print("1.Login")
    print("2.New account")
    option = input("Select option:")

    if option == "2":  
        acc = new_account()
        if not acc:
            main()
            return
        print("Account created. Login")
        option = "1"

    if option != "1":
        print("Invalid option selected")
        sleep(1)
        main()
        return
    
    account = login()

    if not account:
        main()
        return

    print("=" * 80)
    print("Welcome")
    print("=" * 80)
    print(f"Your account balance is {account['balance']}")  
    print("1. Deposit")
    print("2. Withdrawal")  
    print("3. Logout")
    option = input("Select option 1, 2 or 3:")

    if option == "1": 
        deposit(account)
        main()
        return
    if option == "2": 
        withdraw(account)
        main()
        return
    

main()