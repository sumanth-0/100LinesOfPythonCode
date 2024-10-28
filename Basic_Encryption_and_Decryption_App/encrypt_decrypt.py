from cryptography.fernet import Fernet

def generate_key():
    """Generate a key for symmetric encryption."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt the contents of the file."""
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
    print("File encrypted successfully.")

def decrypt_file(file_path, key):
    """Decrypt the contents of the file."""
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)
    print("File decrypted successfully.")

def main():
    action = input("Type 'encrypt' to encrypt a file or 'decrypt' to decrypt a file: ").lower()
    file_path = input("Enter the file path: ")
    key = input("Enter the encryption key (or generate a new one): ")

    if action == 'encrypt':
        encrypt_file(file_path, key.encode())
    elif action == 'decrypt':
        decrypt_file(file_path, key.encode())
    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
