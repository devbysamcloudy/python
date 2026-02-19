from decorators import log
from accounts import get_account_by_id_no
from time import sleep
@log
def login (attempts = 0,account_attempts = 1):
    if attempts >= 4:
        print("Maximum attempts reached")
        print("Account locked. Contact Customer Service")
        return None
    id_number = input("Enter ID number:")

    account = get_account_by_id_no(id_number)

    if not account:
        seconds= account_attempts
        print(f"......Waiting for next login {seconds} seconds")
        sleep(seconds)
        login(attempts=attempts, account_attempts=account_attempts*2)
        return None
    else:
        print("Bank login successful")
        print("Attempt no", attempts)
        new_attempts = attempts + 1
        print("-"*10)
        print(f"Welcome {account['name']}")
        print("-"*10)
        return True
login()
    
    



    
    