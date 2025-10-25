"""
Password Generator CLI 🔐
-------------------------
Generate strong random passwords with letters, numbers, and symbols.

Usage:
    python password_generator.py
"""

import random
import string


def generate_password(length: int = 12, use_uppercase: bool = True,
                      use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generate a random password.

    Parameters:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_numbers (bool): Include digits
        use_symbols (bool): Include symbols like !@#$%

    Returns:
        str: Randomly generated password
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Base characters (lowercase)
    characters = list(string.ascii_lowercase)

    if use_uppercase:
        characters += list(string.ascii_uppercase)
    if use_numbers:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    # Ensure at least one character from each selected type is included
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    # Fill the rest of the password length
    remaining_length = length - len(password)
    password += random.choices(characters, k=remaining_length)

    # Shuffle to prevent predictable patterns
    random.shuffle(password)
    return "".join(password)


def main() -> None:
    """Main CLI interface to generate passwords."""
    print("🔐 Password Generator CLI")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12

    use_upper = input("Include uppercase letters? (y/n, default y): ").strip().lower() or "y"
    use_numbers = input("Include numbers? (y/n, default y): ").strip().lower() or "y"
    use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() or "y"

    password = generate_password(
        length=length,
        use_uppercase=use_upper == "y",
        use_numbers=use_numbers == "y",
        use_symbols=use_symbols == "y"
    )

    print(f"\n✅ Generated Password:\n{password}\n")


if __name__ == "__main__":
    main()


# """
# Password Generator CLI 🔐
# -------------------------
# Generate strong random passwords with at least one uppercase letter,
# one number, and one symbol.

# Usage:
#     python password_generator.py
# """

# import random
# import string


# def generate_password(length: int = 12) -> str:
#     """
#     Generate a random password ensuring at least:
#       - 1 uppercase letter
#       - 1 number
#       - 1 symbol

#     Parameters:
#         length (int): Length of the password (minimum 4)

#     Returns:
#         str: Randomly generated password
#     """
#     if length < 4:
#         raise ValueError("Password length should be at least 4 characters.")

#     # Mandatory characters
#     password = [
#         random.choice(string.ascii_uppercase),  # at least 1 uppercase
#         random.choice(string.digits),           # at least 1 number
#         random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?")  # at least 1 symbol
#     ]

#     # Remaining characters: lowercase + uppercase + digits + symbols
#     all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
#     remaining_length = length - len(password)
#     password += random.choices(all_chars, k=remaining_length)

#     # Shuffle to avoid predictable patterns
#     random.shuffle(password)
#     return "".join(password)


# def main() -> None:
#     """Main CLI interface to generate passwords."""
#     print("🔐 Password Generator CLI")
#     try:
#         length = int(input("Enter password length (default 12): ") or 12)
#     except ValueError:
#         length = 12

#     password = generate_password(length)
