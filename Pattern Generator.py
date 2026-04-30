# Pattern Generator (Stars & Numbers)

# ----------- Star Patterns -----------
def star_patterns():
    n = int(input("Enter number of rows: "))

    print("\n1. Right Triangle")
    print("2. Inverted Triangle")
    print("3. Pyramid")
    print("4. Diamond")

    ch = input("Choose pattern: ")

    if ch == "1":
        for i in range(1, n+1):
            print("* " * i)

    elif ch == "2":
        for i in range(n, 0, -1):
            print("* " * i)

    elif ch == "3":
        for i in range(1, n+1):
            print(" " * (n-i) + "* " * i)

    elif ch == "4":
        # Upper part
        for i in range(1, n+1):
            print(" " * (n-i) + "* " * i)
        # Lower part
        for i in range(n-1, 0, -1):
            print(" " * (n-i) + "* " * i)

    else:
        print("Invalid choice!")


# ----------- Number Patterns -----------
def number_patterns():
    n = int(input("Enter number of rows: "))

    print("\n1. Increasing Numbers")
    print("2. Continuous Numbers")
    print("3. Pyramid Numbers")

    ch = input("Choose pattern: ")

    if ch == "1":
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()

    elif ch == "2":
        num = 1
        for i in range(1, n+1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()

    elif ch == "3":
        for i in range(1, n+1):
            print(" " * (n-i), end="")
            for j in range(1, i+1):
                print(j, end=" ")
            print()

    else:
        print("Invalid choice!")


# ----------- Main Menu -----------
def menu():
    while True:
        print("\n===== PATTERN GENERATOR =====")
        print("1. Star Patterns")
        print("2. Number Patterns")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            star_patterns()
        elif choice == "2":
            number_patterns()
        elif choice == "3":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice!")


# ----------- Run Program -----------
menu()