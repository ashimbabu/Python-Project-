# Simple Interest & EMI Calculator

import math

# ----------- Simple Interest -----------
def simple_interest():
    print("\n--- Simple Interest Calculator ---")
    try:
        p = float(input("Enter Principal Amount: "))
        r = float(input("Enter Rate of Interest (% per year): "))
        t = float(input("Enter Time (in years): "))

        si = (p * r * t) / 100
        total = p + si

        print(f"\nSimple Interest: {si:.2f}")
        print(f"Total Amount   : {total:.2f}\n")

    except ValueError:
        print("Invalid input!\n")


# ----------- EMI Calculator -----------
def emi_calculator():
    print("\n--- EMI Calculator ---")
    try:
        p = float(input("Enter Loan Amount: "))
        r = float(input("Enter Annual Interest Rate (%): "))
        t = float(input("Enter Loan Tenure (years): "))

        monthly_rate = r / (12 * 100)
        months = t * 12

        emi = (p * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)

        total_payment = emi * months
        interest_paid = total_payment - p

        print(f"\nMonthly EMI     : {emi:.2f}")
        print(f"Total Payment   : {total_payment:.2f}")
        print(f"Total Interest  : {interest_paid:.2f}\n")

    except ValueError:
        print("Invalid input!\n")


# ----------- Menu System -----------
def menu():
    while True:
        print("===== FINANCIAL CALCULATOR =====")
        print("1. Simple Interest Calculator")
        print("2. EMI Calculator")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            simple_interest()
        elif choice == "2":
            emi_calculator()
        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")


# ----------- Run Program -----------
menu()