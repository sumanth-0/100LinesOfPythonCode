from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from os import urandom
import base64

# Key derivation function to generate a secure AES key from a password
def generate_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password)

# Encrypt a file with AES256 encryption
def encrypt_file(password: str, input_file: str, output_file: str) -> None:
    salt = urandom(16)  # Generate a random salt for key derivation
    key = generate_key(password.encode(), salt)
    iv = urandom(16)  # Initialization vector for AES

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.write(salt + iv)  # Store salt and IV at the beginning of the file
        while chunk := f_in.read(1024):
            padded_data = padder.update(chunk)
            f_out.write(encryptor.update(padded_data))
        f_out.write(encryptor.update(padder.finalize()) + encryptor.finalize())

# Decrypt a file with AES256 encryption
def decrypt_file(password: str, input_file: str, output_file: str) -> None:
    with open(input_file, 'rb') as f_in:
        salt = f_in.read(16)  # Read the salt and IV
        iv = f_in.read(16)
        key = generate_key(password.encode(), salt)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()

        with open(output_file, 'wb') as f_out:
            while chunk := f_in.read(1024):
                decrypted_data = decryptor.update(chunk)
                unpadded_data = unpadder.update(decrypted_data)
                f_out.write(unpadded_data)
            
            # Finalize decryption and unpad the remaining data
            decrypted_data = decryptor.finalize()
            f_out.write(unpadder.update(decrypted_data) + unpadder.finalize())


# Example usage
# Encrypting a file
encrypt_file(password="yourpassword", input_file="plain.txt", output_file="encrypted.aes")
# Decrypting a file
decrypt_file(password="yourpassword", input_file="encrypted.aes", output_file="decrypted.txt")
