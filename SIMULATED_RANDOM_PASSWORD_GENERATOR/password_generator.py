import random
import string

def generate_password(length=12, use_special_chars=True):
    """Generate a random password with specified length and options."""
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter desired password length (default is 12): ") or 12)
    use_special_chars = input("Include special characters? (yes/no, default is yes): ").strip().lower() != 'no'
    
    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
