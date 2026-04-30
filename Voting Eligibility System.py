# Voting Eligibility System

def check_eligibility():
    print("\n===== VOTING ELIGIBILITY CHECK =====")
    
    name = input("Enter your name: ")
    
    try:
        age = int(input("Enter your age: "))
        citizenship = input("Are you a citizen? (yes/no): ").lower()

        if age < 0:
            print("❌ Invalid age!\n")
            return

        print("\n--- RESULT ---")

        if age >= 18 and citizenship == "yes":
            print(f"✅ {name}, you are eligible to vote.")
        else:
            print(f"❌ {name}, you are NOT eligible to vote.")

        # Additional info
        if age < 18:
            print("Reason: Must be at least 18 years old.")
        if citizenship != "yes":
            print("Reason: Must be a citizen.")

        print("-----------------------------\n")

    except ValueError:
        print("❌ Invalid input! Age must be a number.\n")


def menu():
    while True:
        print("===== VOTING SYSTEM =====")
        print("1. Check Voting Eligibility")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_eligibility()
        elif choice == "2":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run Program
menu()