# Simple ATM Simulation

import getpass

# ------------------ Account Data ------------------
account = {
    "name": "Ashim",
    "pin": "1234",
    "balance": 10000
}

# ------------------ Authentication ------------------
def authenticate():
    print("\n===== ATM LOGIN =====")
    for attempt in range(3):
        pin = getpass.getpass("Enter your 4-digit PIN: ")
        if pin == account["pin"]:
            print("\nLogin successful!\n")
            return True
        else:
            print("Incorrect PIN.")
    print("\nToo many incorrect attempts. Card blocked.")
    return False

# ------------------ ATM Operations ------------------

def check_balance():
    print(f"\nYour current balance is: NPR {account['balance']}")


def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount.")
            return
        account["balance"] += amount
        print(f"Deposit successful. New balance: NPR {account['balance']}")
    except ValueError:
        print("Enter a valid number.")


def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > account["balance"]:
            print("Insufficient balance.")
        else:
            account["balance"] -= amount
            print(f"Withdrawal successful. Remaining balance: NPR {account['balance']}")
    except ValueError:
        print("Enter a valid number.")


def change_pin():
    current = getpass.getpass("Enter current PIN: ")
    if current != account["pin"]:
        print("Incorrect current PIN.")
        return

    new_pin = getpass.getpass("Enter new PIN: ")
    confirm = getpass.getpass("Confirm new PIN: ")

    if new_pin == confirm:
        account["pin"] = new_pin
        print("PIN successfully changed.")
    else:
        print("PIN mismatch.")

# ------------------ Menu ------------------

def atm_menu():
    while True:
        print("""
===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Change PIN
5. Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("\nThank you for using the ATM.")
            break
        else:
            print("Invalid option.")

# ------------------ Main ------------------

if __name__ == "__main__":
    if authenticate():
        atm_menu()
