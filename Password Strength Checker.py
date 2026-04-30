# Password Strength Checker

import re

def check_password_strength(password):
    score = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        remarks += "❌ Password should be at least 8 characters long.\n"

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks += "❌ Add lowercase letters.\n"

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks += "❌ Add uppercase letters.\n"

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        remarks += "❌ Add numbers.\n"

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks += "❌ Add special characters.\n"

    # Strength evaluation
    if score == 5:
        strength = "🔐 Strong Password"
    elif score >= 3:
        strength = "⚠️ Medium Password"
    else:
        strength = "❌ Weak Password"

    return strength, remarks


def main():
    print("===== PASSWORD STRENGTH CHECKER =====")

    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nResult:", strength)

    if feedback:
        print("\nSuggestions:")
        print(feedback)


if __name__ == "__main__":
    main()