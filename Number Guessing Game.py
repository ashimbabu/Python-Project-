import random
import time

# ------------------ Game Settings ------------------
MAX_ATTEMPTS = 7
LOW = 1
HIGH = 100

# ------------------ Utility ------------------

def loading(msg="Processing"):
    print(f"\n{msg}", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

# ------------------ Difficulty ------------------

def choose_difficulty():
    print("\nSelect Difficulty")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    choice = input("Choose option: ")

    if choice == "1":
        return 1, 50, 10
    elif choice == "2":
        return 1, 100, 7
    elif choice == "3":
        return 1, 200, 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 1, 100, 7

# ------------------ Game Logic ------------------

def play_game():
    low, high, attempts = choose_difficulty()

    secret = random.randint(low, high)
    tries = 0

    print(f"\nGuess the number between {low} and {high}")

    while tries < attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        tries += 1

        if guess == secret:
            loading("Checking")
            print(f"🎉 Correct! You guessed it in {tries} attempts!")
            return

        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        print(f"Attempts left: {attempts - tries}")

    loading("Game Over")
    print(f"❌ You ran out of attempts. The number was {secret}.")

# ------------------ Menu ------------------

def menu():
    while True:
        print("\n====== NUMBER GUESSING GAME ======")
        print("1. Play Game")
        print("2. Game Rules")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("""
Game Rules:
- The computer selects a random number.
- You must guess the number within limited attempts.
- After each guess, you will receive hints (Too high / Too low).
- Choose difficulty to change number range and attempts.
""")
        elif choice == "3":
            print("\nThanks for playing!")
            break
        else:
            print("Invalid option.")

# ------------------ Start Game ------------------
if __name__ == "__main__":
    menu()
