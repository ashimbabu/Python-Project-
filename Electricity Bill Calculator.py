# Electricity Bill Calculator

def calculate_bill(units):
    bill = 0

    # Slab rates (customizable)
    if units <= 100:
        bill = units * 8
    elif units <= 200:
        bill = (100 * 8) + (units - 100) * 9.5
    else:
        bill = (100 * 8) + (100 * 9.5) + (units - 200) * 12

    # Additional charges
    service_charge = 50
    tax = 0.05 * bill   # 5% tax

    total = bill + service_charge + tax

    return bill, service_charge, tax, total


def generate_bill():
    print("\n===== ELECTRICITY BILL CALCULATOR =====")

    name = input("Enter Customer Name: ")
    meter_no = input("Enter Meter Number: ")

    try:
        units = float(input("Enter Units Consumed: "))
        if units < 0:
            print("Units cannot be negative!")
            return
    except ValueError:
        print("Invalid input!")
        return

    bill, service, tax, total = calculate_bill(units)

    print("\n========== BILL DETAILS ==========")
    print(f"Customer Name : {name}")
    print(f"Meter Number  : {meter_no}")
    print(f"Units Used    : {units}")
    print(f"Energy Charge : NPR {bill:.2f}")
    print(f"Service Charge: NPR {service:.2f}")
    print(f"Tax (5%)      : NPR {tax:.2f}")
    print("----------------------------------")
    print(f"TOTAL BILL    : NPR {total:.2f}")
    print("==================================\n")


def menu():
    while True:
        print("===== MENU =====")
        print("1. Generate Bill")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_bill()
        elif choice == "2":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run Program
menu()