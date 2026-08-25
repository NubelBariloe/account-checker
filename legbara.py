import json
from random import randint

def create():
    name = input("Enter account name: ")
    try:
        with open("account_details.json", "r", encoding="utf-8") as file:
            account_details = json.load(file)

    except (FileNotFoundError,  json.JSONDecodeError):
        account_details = []

    number_exist = False
    number = randint(0000000000, 9999999999)

    while number_exist:
        for account in account_details:
            if account["number"] == number:
                number_exist = True
                print("account already exists")

        if not number_exist:
            break
    pin = int(input("Enter account pin: "))


    new_account = {
        "name": name,
        "number": number,
        "balance": 0,
        "pin": pin
        }

    account_details.append(new_account)

    with open("account_details.json", "w", encoding="utf-8") as file:
        json.dump(account_details, file, indent=4)
    print("Account created successfully")
    print(f"your new account number is {number}\n"
          f"your account name is {name}\n"
          f"and your balance is {new_account['balance']}")

def deposit():
    with open("account_details.json", "r", encoding="utf-8") as file:
        account_details = json.load(file)
    number = int(input("Enter account number: "))
    for account in account_details:
        if account["number"] == number:
            add = int(input("enter the amount you wish to deposit: "))
            account["balance"] += add
            with open("account_details.json", "w", encoding="utf-8") as file:
                json.dump(account_details, file, indent=4)
            print("Account deposited successfully")

def withdraw():
    with open("account_details.json", "r", encoding="utf-8") as file:
        account_details = json.load(file)
    number = int(input("Enter account number: "))
    for account in account_details:
        if account["number"] == number:
            pin = int(input("Enter account pin: "))
            if account["pin"] == pin:
                add = int(input("enter the amount you wish to withdraw : "))
                if account["balance"] < add:
                    print("You don't have enough money to withdraw")
                else:
                    account["balance"] -= add
                    with open("account_details.json", "w", encoding="utf-8") as file:
                        json.dump(account_details, file, indent=4)
                        print("withdrawal successful")
            else:
                print("wrong account pin")

def transfer():
    with open("account_details.json", "r", encoding="utf-8") as file:
        account_details = json.load(file)
    sender = int(input("Enter sender account number: "))
    for account in account_details:
        if account["number"] == sender:
            receiver = int(input("Enter receiver account number: "))
            if receiver == sender:
                print("You can't transfer money to yourself")
            else:
                pin = int(input("Enter account pin: "))
                if account["pin"] == pin:
                    amount = int(input("Enter amount to transfer: "))
                    if amount > account["balance"]:
                        print("insufficient funds")
                    else:
                        account["balance"] -= amount
                        for number in account_details:
                            if number["number"] == receiver:
                                number["balance"] += amount
                                with open("account_details.json", "w", encoding="utf-8") as file:
                                    json.dump(account_details, file, indent=4)
                                    print("transfer successful")
                else:
                    print("wrong account pin")


def check_balance():
    with open("account_details.json", "r", encoding="utf-8") as file:
        account_details = json.load(file)
    number = int(input("Enter your account number: "))
    for account in account_details:
        if account["number"] == number:
            print("Your account balance is: ", account["balance"])
ben = True
while ben:
    options = input("Please enter your options:\n"
                    "1. Create Account\n"
                    "2. Deposit\n"
                    "3. Withdraw\n"
                    "4. Transfer\n"
                    "5. Check Balance\n"
                    "6. Quit \n")

    if options == "1":
        create()
    elif options == "2":
        deposit()
    elif options == "3":
        withdraw()
    elif options == "4":
        transfer()
    elif options == "5":
        check_balance()
    else:
        ben = False

