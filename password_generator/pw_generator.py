import hashlib
import os
import json

# Function to generate a hashed password with PBKDF2 and return the salt and hash
def generate_pbkdf2_password(secret, salt=None, iterations=100000, dklen=16):
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt if not provided
    hashed_password = hashlib.pbkdf2_hmac('sha256', secret.encode(), salt, iterations, dklen).hex()
    return salt.hex(), hashed_password

# Function to verify a password against a stored hash and salt
def verify_password(stored_password, stored_salt, input_password, iterations=100000, dklen=16):
    input_salt = bytes.fromhex(stored_salt)
    _, input_hashed_password = generate_pbkdf2_password(input_password, input_salt, iterations, dklen)
    return input_hashed_password == stored_password

# Function to store user credentials (username, salt, hashed password) in a JSON file
def store_user(username, salt, hashed_password):
    user_data = {username: {"salt": salt, "password": hashed_password}}
    with open("users.json", "a") as file:
        file.write(json.dumps(user_data) + "\n")
    print(f"User {username} successfully registered!")

# Function to load stored user data from the JSON file
def load_users():
    users = {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            for line in file:
                user = json.loads(line)
                users.update(user)
    return users

# Function to handle user sign-up
def user_signup():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    salt, hashed_password = generate_pbkdf2_password(password)
    store_user(username, salt, hashed_password)

# Function to handle user login
def user_login():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        stored_salt = users[username]["salt"]
        stored_password = users[username]["password"]
        if verify_password(stored_password, stored_salt, password):
            print(f"Welcome back, {username}! Login successful.")
        else:
            print("Incorrect password. Login failed.")
    else:
        print(f"User {username} not found.")

# Main menu for user interaction
def main():
    while True:
        print("\n1) Sign Up\n2) Log In\n3) Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            user_signup()
        elif choice == '2':
            user_login()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
