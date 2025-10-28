
import json, os, sys, base64
from getpass import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from pathlib import Path

VAULT_FILE = Path.home() / ".tiny_vault.bin"
SALT_SIZE = 16
ITER = 390000

def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=ITER, backend=default_backend())
    return base64.urlsafe_b64encode(kdf.derive(password))

def init_vault():
    if VAULT_FILE.exists():
        return
    pwd = getpass("Create a master password: ").encode()
    pwd2 = getpass("Confirm your password: ").encode()
    if pwd != pwd2:
        print("Both passwords don't match."); sys.exit(1)
    salt = os.urandom(SALT_SIZE)
    key = derive_key(pwd, salt)
    f = Fernet(key)
    empty = json.dumps({}).encode()
    blob = base64.b64encode(salt + f.encrypt(empty))
    VAULT_FILE.write_bytes(blob)
    print("Vault is created:", VAULT_FILE)

def load_vault():
    if not VAULT_FILE.exists():
        print("No vault found. Initializing a new vault.")
        init_vault()
    raw = base64.b64decode(VAULT_FILE.read_bytes())
    salt, ct = raw[:SALT_SIZE], raw[SALT_SIZE:]
    pwd = getpass("Your Master password is: ").encode()
    key = derive_key(pwd, salt)
    f = Fernet(key)
    try:
        data = json.loads(f.decrypt(ct).decode())
    except Exception:
        print("This is an invalid password or corrupted vault."); sys.exit(1)
    return data, salt, key

def save_vault(data, salt, key):
    f = Fernet(key)
    ct = f.encrypt(json.dumps(data).encode())
    VAULT_FILE.write_bytes(base64.b64encode(salt + ct))

def prompt_loop(data, salt, key):
    HELP = "Commands: add, get, list, del, exit, help"
    print(HELP)
    while True:
        cmd = input("vault> ").strip().split(maxsplit=1)
        if not cmd: continue
        op = cmd[0].lower()
        arg = cmd[1] if len(cmd) > 1 else ""
        if op in ("exit","quit"):
            save_vault(data, salt, key); print("Saved. Bye."); break
        if op == "help":
            print(HELP); continue
        if op == "list":
            for name in sorted(data.keys()):
                print("-", name)
            continue
        if op == "add":
            name = arg or input("name: ").strip()
            user = input("username (optional): ").strip()
            pwd = getpass("password (leave empty to generate): ").strip()
            if not pwd:
                import secrets, string
                pwd = ''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(16))
                print("Generated:", pwd)
            notes = input("notes (optional): ").strip()
            data[name] = {"user": user, "password": pwd, "notes": notes}
            save_vault(data, salt, key); print("Saved.")
            continue
        if op == "get":
            name = arg or input("name: ").strip()
            e = data.get(name)
            if not e: print("Not found."); continue
            print("username:", e.get("user",""))
            print("password:", e.get("password",""))
            print("notes:", e.get("notes",""))
            continue
        if op in ("del","delete","rm"):
            name = arg or input("name: ").strip()
            if name in data:
                confirm = input(f"Delete {name}? (y/N): ").lower()
                if confirm == "y":
                    del data[name]; save_vault(data, salt, key); print("Deleted.")
                else:
                    print("Aborted.")
            else:
                print("Not found.")
            continue
        print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    init_vault() 
    data, salt, key = load_vault()
    prompt_loop(data, salt, key)
