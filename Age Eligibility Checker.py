# Age Eligibility Checker

def check_eligibility(age):
    print("\n===== ELIGIBILITY RESULTS =====")

    # Voting eligibility
    if age >= 18:
        print("🗳 Eligible to Vote")
    else:
        print("❌ Not eligible to Vote")

    # Driving eligibility
    if age >= 18:
        print("🚗 Eligible for Driving License")
    else:
        print("❌ Not eligible for Driving License")

    # Job eligibility
    if age >= 18:
        print("💼 Eligible for Employment")
    else:
        print("❌ Not eligible for Employment")

    # Senior citizen
    if age >= 60:
        print("👴 Senior Citizen Benefits Applicable")

    print("================================\n")


def menu():
    while True:
        print("===== AGE ELIGIBILITY CHECKER =====")
        print("1. Check Eligibility")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                age = int(input("Enter your age: "))
                if age < 0:
                    print("Age cannot be negative!\n")
                else:
                    check_eligibility(age)
            except ValueError:
                print("Invalid input! Please enter a valid number.\n")

        elif choice == "2":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
menu()