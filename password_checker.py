import random
import string

def check_password_strength(password):
    if not password:
        return "Invalid", ["Password cannot be empty!"], {}
    if len(password) > 50:
        return "Invalid", ["Password is too long (max 50 characters)!"], {}

    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    upper_count = 0
    lower_count = 0
    digit_count = 0
    special_count = 0

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for char in password:
        if char.isupper():
            has_upper = True
            upper_count += 1
        elif char.islower():
            has_lower = True
            lower_count += 1
        elif char.isdigit():
            has_digit = True
            digit_count += 1
        elif char in special_chars:
            has_special = True
            special_count += 1

    overview = {
        "Uppercase Letters": upper_count,
        "Lowercase Letters": lower_count,
        "Digits": digit_count,
        "Special Characters": special_count,
        "Total Length": length
    }

    score = 0
    feedback = []

    if length >= 12:
        score += 3
    elif length >= 8:
        score += 2
    else:
        feedback.append("Password should be at least 8 characters long")

    if has_upper:
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if has_lower:
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if has_digit:
        score += 1
    else:
        feedback.append("Add at least one digit")

    if has_special:
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%)")

    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback, overview


def generate_suggested_password():
    length = 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice("!@#$%^&*()") +
        ''.join(random.choice(chars) for _ in range(length - 4))
    )
    password = ''.join(random.sample(password, len(password)))
    return password


def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")


def main():
    print_colored("Welcome to Enhanced Password Strength Checker!", "1;34")
    print("----------------------------------------")

    while True:
        print("\nOptions:")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            password = input("\nEnter your password: ")
            strength, feedback, overview = check_password_strength(password)

            if strength == "Very Strong":
                color = "1;32"
            elif strength == "Strong":
                color = "1;32"
            elif strength == "Medium":
                color = "1;33"
            elif strength == "Weak":
                color = "1;31"
            else:
                color = "1;31"

            print_colored(f"\nPassword Strength: {strength}", color)

            strength_levels = {"Very Strong": 8, "Strong": 6, "Medium": 4, "Weak": 2, "Invalid": 0}
            bar_length = strength_levels.get(strength, 0)
            print("Strength Level: [" + "=" * bar_length + " " * (8 - bar_length) + "]")

            print("\nPassword Overview:")
            for key, value in overview.items():
                print(f"- {key}: {value}")

            if feedback:
                print("\nSuggestions to improve your password:")
                for suggestion in feedback:
                    print("- " + suggestion)
            else:
                print("\nYour password is excellent and meets all criteria!")

        elif choice == "2":
            suggested_password = generate_suggested_password()
            print_colored(f"\nSuggested Strong Password: {suggested_password}", "1;32")
            strength, _, _ = check_password_strength(suggested_password)
            print(f"Strength: {strength}")

        elif choice == "3":
            print_colored("\nThank you for using Password Strength Checker!", "1;34")
            break

        else:
            print_colored("\nInvalid choice! Please select 1, 2, or 3.", "1;31")


if __name__ == "__main__":
    main()
