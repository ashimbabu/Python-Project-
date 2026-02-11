
# Smart Calculator (Menu-Driven)

import math
import time
from datetime import datetime

# ------------------ Utilities ------------------

def loading():
    print("\nCalculating", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

# ------------------ Menus ------------------

def main_menu():
    print("\n========= SMART CALCULATOR =========")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculator")
    print("3. Statistical Calculator")
    print("4. Financial Calculator")
    print("5. Unit Converter")
    print("6. History")
    print("7. Exit")

# ------------------ History ------------------

history = []

def add_history(op, result):
    history.append({
        "operation": op,
        "result": result,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# ------------------ Basic Arithmetic ------------------

def basic_arithmetic():
    print("\n--- Basic Arithmetic ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    ch = input("Choose: ")
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))

    if ch == "1":
        res = a + b
        op = f"{a} + {b}"
    elif ch == "2":
        res = a - b
        op = f"{a} - {b}"
    elif ch == "3":
        res = a * b
        op = f"{a} * {b}"
    elif ch == "4":
        if b == 0:
            print("Division by zero error!")
            return
        res = a / b
        op = f"{a} / {b}"
    else:
        print("Invalid Option")
        return

    loading()
    print("Result:", res)
    add_history(op, res)

# ------------------ Scientific Calculator ------------------

def scientific():
    print("\n--- Scientific Calculator ---")
    print("1. Square Root")
    print("2. Power")
    print("3. Logarithm")
    print("4. Sin")
    print("5. Cos")
    print("6. Tan")

    ch = input("Choose: ")

    if ch == "1":
        x = float(input("Enter Number: "))
        res = math.sqrt(x)
        op = f"sqrt({x})"

    elif ch == "2":
        a = float(input("Base: "))
        b = float(input("Power: "))
        res = math.pow(a, b)
        op = f"{a}^{b}"

    elif ch == "3":
        x = float(input("Enter Number: "))
        res = math.log(x)
        op = f"log({x})"

    elif ch == "4":
        x = float(input("Angle in degrees: "))
        res = math.sin(math.radians(x))
        op = f"sin({x})"

    elif ch == "5":
        x = float(input("Angle in degrees: "))
        res = math.cos(math.radians(x))
        op = f"cos({x})"

    elif ch == "6":
        x = float(input("Angle in degrees: "))
        res = math.tan(math.radians(x))
        op = f"tan({x})"

    else:
        print("Invalid Option")
        return

    loading()
    print("Result:", res)
    add_history(op, res)

# ------------------ Statistical Calculator ------------------

def statistics_calc():
    print("\n--- Statistical Calculator ---")
    nums = list(map(float, input("Enter numbers separated by space: ").split()))

    mean = sum(nums)/len(nums)
    variance = sum((x-mean)**2 for x in nums)/len(nums)
    std = math.sqrt(variance)

    loading()
    print("Mean      :", mean)
    print("Variance  :", variance)
    print("Std Dev   :", std)

    add_history("Statistics", {"mean":mean,"variance":variance,"std":std})

# ------------------ Financial Calculator ------------------

def financial_calc():
    print("\n--- Financial Calculator ---")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Loan EMI")

    ch = input("Choose: ")

    if ch == "1":
        p = float(input("Principal: "))
        r = float(input("Rate (%): "))
        t = float(input("Time (years): "))
        res = (p*r*t)/100
        op = "Simple Interest"

    elif ch == "2":
        p = float(input("Principal: "))
        r = float(input("Rate (%): "))
        t = float(input("Time (years): "))
        res = p * ((1 + r/100) ** t)
        op = "Compound Interest"

    elif ch == "3":
        p = float(input("Loan Amount: "))
        r = float(input("Annual Interest Rate (%): "))
        n = float(input("Time (years): "))
        r_month = r / (12*100)
        n_month = n * 12
        res = (p*r_month*(1+r_month)**n_month)/((1+r_month)**n_month-1)
        op = "Loan EMI"

    else:
        print("Invalid Option")
        return

    loading()
    print("Result:", res)
    add_history(op, res)

# ------------------ Unit Converter ------------------

def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. KM to Miles")
    print("2. Miles to KM")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    ch = input("Choose: ")
    x = float(input("Enter Value: "))

    if ch == "1":
        res = x * 0.621371
        op = "KM to Miles"
    elif ch == "2":
        res = x / 0.621371
        op = "Miles to KM"
    elif ch == "3":
        res = (x * 9/5) + 32
        op = "C to F"
    elif ch == "4":
        res = (x - 32) * 5/9
        op = "F to C"
    else:
        print("Invalid Option")
        return

    loading()
    print("Result:", res)
    add_history(op, res)

# ------------------ History Viewer ------------------

def view_history():
    print("\n====== Calculation History ======")
    if not history:
        print("No history found")
        return

    for i, h in enumerate(history,1):
        print(f"{i}. {h['time']} | {h['operation']} = {h['result']}")

# ------------------ Main System ------------------

def smart_calculator():
    while True:
        main_menu()
        ch = input("\nChoose Option (1-7): ")

        if ch == "1":
            basic_arithmetic()
        elif ch == "2":
            scientific()
        elif ch == "3":
            statistics_calc()
        elif ch == "4":
            financial_calc()
        elif ch == "5":
            unit_converter()
        elif ch == "6":
            view_history()
        elif ch == "7":
            print("\nExiting Smart Calculator...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
smart_calculator()
