
# PBKDF2 Password Generator and Verifier

This project implements a **PBKDF2-based password generator** and **password verification system** using Python. It allows users to securely hash passwords using the PBKDF2 key derivation function, and then verify those passwords later using the stored hash and salt.

## Features

- **PBKDF2 Password Hashing**: Securely hashes passwords using the PBKDF2 algorithm with HMAC and SHA-256.
- **Salt Generation**: Random salt generation for each password to ensure that identical passwords don't produce the same hash.
- **Password Verification**: Verifies input passwords by comparing them with stored hashed passwords.
- **User Sign-Up and Login**: A simple simulation of user sign-up and login, where passwords are stored as salted hashes.
- **File Storage**: Stores user credentials (username, salt, and password hash) in a JSON file.

## Tools and Libraries

- **hashlib**: Used for PBKDF2 password hashing.
- **os**: For generating random salts.
- **json**: To store and load user credentials.
- **Python 3.x**: The project is built using Python 3.x.

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:sumanth-0/100LinesOfPythonCode.git
    ```

2. No external libraries are required to install. This project works with Python's standard library.

3. Run the program:
    ```bash
    python password_generator.py
    ```

## Usage

- After running the program, you will be presented with a simple menu:
  - **Sign Up**: Create a new user by entering a username and password. The password is hashed and stored securely in the `users.json` file.
  - **Log In**: Enter your username and password to verify the credentials stored in the system.
  - **Exit**: Quit the program.

### Example

```
1) Sign Up
2) Log In
3) Exit
Choose an option: 1
Enter a username: alice
Enter a password: my_secure_password
User alice successfully registered!

1) Sign Up
2) Log In
3) Exit
Choose an option: 2
Enter your username: alice
Enter your password: my_secure_password
Welcome back, alice! Login successful.
```

## How It Works

- The `generate_pbkdf2_password` function creates a salted hash of the user's password using the PBKDF2 algorithm with 100,000 iterations.
- The generated hash and salt are stored in a `users.json` file.
- When the user attempts to log in, the stored salt is retrieved, and the entered password is hashed again and compared to the stored hash to verify its validity.

## License

This project is licensed under the MIT License.

## Contribution

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## Contact

For any queries or issues, please reach out at your-email@example.com.
