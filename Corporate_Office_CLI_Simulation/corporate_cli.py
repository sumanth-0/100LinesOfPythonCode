
"""
Simple console employee workflow system demonstrating
inheritance & polymorphism + file handling.

- Vim-like save: enter lines, then type ':wq' on a new line to save.
- Cancel entry with ':q!' on a new line.
"""

import os
import shutil
import getpass
from datetime import datetime

ROOT_DIR = os.path.abspath(".")
USERS_FILE = os.path.join(ROOT_DIR, "users.txt")

# Roles and default substructure
ROLES = {
    "Manager": [],
    "Developer": ["Frontend", "Backend"],
    "Intern": [],
    "HR": []
}

# Utility functions


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause(msg="Press Enter to continue..."):
    input(msg)


def ensure_dirs():
    """Create root role directories and users file if missing."""
    if not os.path.exists(USERS_FILE):
        # create users file and write default admin
        with open(USERS_FILE, "w") as f:
            f.write("admin:Admin:admin123\n")
        print("Created users.txt with default admin (username=admin, password=admin123).")

    for role, subs in ROLES.items():
        role_path = os.path.join(ROOT_DIR, role)
        os.makedirs(role_path, exist_ok=True)
        if subs:
            for s in subs:
                os.makedirs(os.path.join(role_path, s), exist_ok=True)


def read_users():
    """Return dict username -> (role, password)."""
    users = {}
    if not os.path.exists(USERS_FILE):
        return users
    with open(USERS_FILE, "r") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split(":", 2)
            if len(parts) == 3:
                username, role, password = parts
                users[username] = (role, password)
    return users


def add_user_to_file(username, role, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username}:{role}:{password}\n")


def ensure_user_dirs(role, username, sub_role=None):
    """Create directory for user and Pending/Accepted/Rejected."""
    if sub_role:
        base = os.path.join(ROOT_DIR, role, sub_role, username)
    else:
        # if role has subfolders but none provided, put directly under role
        base = os.path.join(ROOT_DIR, role, username)
    for sub in ("Pending", "Accepted", "Rejected"):
        os.makedirs(os.path.join(base, sub), exist_ok=True)
    return base


def timestamped_filename(base_name, username):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c for c in base_name if c.isalnum() or c in (" ", "_", "-")).rstrip()
    return f"{username}_{safe}_{now}.txt"


def list_files(path):
    try:
        files = sorted(os.listdir(path))
    except FileNotFoundError:
        files = []
    return files


# Base classes


class Employee:
    def __init__(self, username, role, sub_role=None):
        self.username = username
        self.role = role
        self.sub_role = sub_role  # For Developer: Frontend/Backend or None
        # ensure directory
        self.base_dir = ensure_user_dirs(role, username, sub_role)

    def menu(self):
        """Show employee menu. Polymorphism: different classes may override."""
        while True:
            clear_screen()
            print(f"Logged in as: {self.username} ({self.role}{'/' + self.sub_role if self.sub_role else ''})")
            print("1) Log new work")
            print("2) Resubmit rejected work")
            print("3) Check completed work (Accepted)")
            print("4) Logout")
            choice = input("Choose: ").strip()
            if choice == "1":
                self.log_new_work()
            elif choice == "2":
                self.resubmit_rejected()
            elif choice == "3":
                self.check_completed()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
                pause()

    def _enter_multiline(self):
        """
        Collect multiline text from the user.
        Use ':wq' on its own line to save.
        Use ':q!' on its own line to cancel.
        """
        print("Enter your work below. Write ':wq' alone on a line to save, ':q!' alone to cancel.")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:  # handle ctrl-D gracefully
                print("\nEOF detected — cancelling.")
                return None
            if line.strip() == ":wq":
                return "\n".join(lines)
            if line.strip() == ":q!":
                return None
            lines.append(line)

    def log_new_work(self):
        clear_screen()
        print("Log New Work")
        base_name = input("Enter short name for the work (no extension): ").strip()
        if not base_name:
            print("Invalid name.")
            pause()
            return
        content = self._enter_multiline()
        if content is None:
            print("Work entry cancelled.")
            pause()
            return
        fname = timestamped_filename(base_name, self.username)
        pending_dir = os.path.join(self.base_dir, "Pending")
        path = os.path.join(pending_dir, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Author: {self.username}\nTime: {datetime.now().isoformat()}\n\n")
            f.write(content)
        print(f"Saved to {path}")
        pause()

    def resubmit_rejected(self):
        clear_screen()
        rej_dir = os.path.join(self.base_dir, "Rejected")
        files = list_files(rej_dir)
        if not files:
            print("No rejected work to resubmit.")
            pause()
            return
        print("Rejected files:")
        for i, fn in enumerate(files, 1):
            print(f"{i}) {fn}")
        sel = input("Select file number to resubmit (or blank to cancel): ").strip()
        if not sel:
            return
        try:
            idx = int(sel) - 1
            if idx < 0 or idx >= len(files):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            pause()
            return
        src = os.path.join(rej_dir, files[idx])
        with open(src, "r", encoding="utf-8") as f:
            original = f.read()
        print("You may edit the content before resubmitting. Current content shown below:")
        print("-" * 40)
        print(original)
        print("-" * 40)
        print("Enter additional notes or edit lines. Use ':wq' on its own line to finish, ':q!' to cancel and keep original.")
        extra = self._enter_multiline()
        if extra is None:
            print("Resubmit cancelled.")
            pause()
            return
        # Create a new pending file with resubmission note
        pending_dir = os.path.join(self.base_dir, "Pending")
        base_name = f"resub_{os.path.splitext(files[idx])[0]}"
        fname = timestamped_filename(base_name, self.username)
        dst = os.path.join(pending_dir, fname)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(f"Author: {self.username}\nResubmittedTime: {datetime.now().isoformat()}\n\n")
            f.write(original + "\n\n--- Resubmit Notes ---\n")
            f.write(extra)
        print(f"Resubmitted to {dst}")
        pause()

    def check_completed(self):
        clear_screen()
        acc_dir = os.path.join(self.base_dir, "Accepted")
        files = list_files(acc_dir)
        if not files:
            print("No accepted/completed work.")
            pause()
            return
        print("Completed files:")
        for i, fn in enumerate(files, 1):
            print(f"{i}) {fn}")
        sel = input("Enter file number to view (or blank to cancel): ").strip()
        if not sel:
            return
        try:
            idx = int(sel) - 1
            if idx < 0 or idx >= len(files):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            pause()
            return
        path = os.path.join(acc_dir, files[idx])
        clear_screen()
        print(f"--- {files[idx]} ---")
        with open(path, "r", encoding="utf-8") as f:
            print(f.read())
        print("--- end ---")
        pause()


class Admin(Employee):
    def menu(self):
        while True:
            clear_screen()
            print(f"Admin console — {self.username}")
            print("1) Add new employee")
            print("2) View pending work")
            print("3) Logout")
            choice = input("Choose: ").strip()
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_pending_and_action()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
                pause()

    def add_employee(self):
        clear_screen()
        print("Add New Employee")
        username = input("Enter username: ").strip()
        if not username:
            print("Invalid username.")
            pause()
            return
        users = read_users()
        if username in users:
            print("User already exists.")
            pause()
            return
        print("Available roles:")
        for i, r in enumerate(ROLES.keys(), 1):
            print(f"{i}) {r}")
        role_sel = input("Select role number: ").strip()
        try:
            role_idx = int(role_sel) - 1
            role = list(ROLES.keys())[role_idx]
        except Exception:
            print("Invalid role selection.")
            pause()
            return
        sub_role = None
        if ROLES[role]:
            print(f"{role} has sub-roles:")
            for i, s in enumerate(ROLES[role], 1):
                print(f"{i}) {s}")
            sub_sel = input("Select sub-role number (or blank to skip): ").strip()
            if sub_sel:
                try:
                    sub_idx = int(sub_sel) - 1
                    sub_role = ROLES[role][sub_idx]
                except Exception:
                    print("Invalid sub-role selection.")
                    pause()
                    return
        password = getpass.getpass("Enter password for new user: ").strip()
        if not password:
            print("Password cannot be blank.")
            pause()
            return
        # Persist
        add_user_to_file(username, role if not sub_role else f"{role}/{sub_role}", password)
        # Create dir structure; if sub_role provided, ensure correct nesting
        if sub_role:
            ensure_user_dirs(role, username, sub_role)
        else:
            ensure_user_dirs(role, username, None)
        print(f"Added user {username} with role {role}{('/'+sub_role) if sub_role else ''}")
        pause()

    def view_pending_and_action(self):
        clear_screen()
        print("View Pending Work Across All Users")
        users = read_users()
        # Collect pending files across roles
        pending_map = []  # list of tuples (role, sub_role, username, filepath, filename)
        for username, (role_full, _) in users.items():
            # skip admin's own account to avoid processing it if desired
            # role_full might be "Developer/Frontend"
            if "/" in role_full:
                role, sub_role = role_full.split("/", 1)
            else:
                role, sub_role = role_full, None
            base = os.path.join(ROOT_DIR, role, sub_role) if sub_role else os.path.join(ROOT_DIR, role)
            user_dir = os.path.join(base, username)
            pending_dir = os.path.join(user_dir, "Pending")
            files = list_files(pending_dir)
            for fn in files:
                pending_map.append((role, sub_role, username, os.path.join(pending_dir, fn), fn))
        if not pending_map:
            print("No pending files available.")
            pause()
            return
        # list files
        for i, (role, sub_role, username, path, fn) in enumerate(pending_map, 1):
            loc = f"{role}{('/' + sub_role) if sub_role else ''}/{username}"
            print(f"{i}) [{loc}] {fn}")
        sel = input("Select file number to review (or blank to cancel): ").strip()
        if not sel:
            return
        try:
            idx = int(sel) - 1
            if idx < 0 or idx >= len(pending_map):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            pause()
            return
        role, sub_role, username, filepath, fn = pending_map[idx]
        clear_screen()
        print(f"Reviewing: {fn} from {username} ({role}{('/' + sub_role) if sub_role else ''})")
        print("-" * 50)
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
        print("-" * 50)
        action = input("Action: (a)ccept / (r)eject / (k)eep pending: ").strip().lower()
        if action == "a":
            dest_dir = os.path.join(ROOT_DIR, role, sub_role, username, "Accepted") if sub_role else os.path.join(ROOT_DIR, role, username, "Accepted")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_dir, fn))
            print("Moved to Accepted.")
        elif action == "r":
            dest_dir = os.path.join(ROOT_DIR, role, sub_role, username, "Rejected") if sub_role else os.path.join(ROOT_DIR, role, username, "Rejected")
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_dir, fn))
            print("Moved to Rejected.")
        else:
            print("Kept pending.")
        pause()


# Other role classes may override methods or add specialized behavior if necessary
class Manager(Employee):
    pass


class Developer(Employee):
    def __init__(self, username, role, sub_role):
        # sub_role expected (Frontend/Backend)
        super().__init__(username, role, sub_role)


class Intern(Employee):
    pass


class HR(Employee):
    pass


# Authentication and factory


def create_employee_object(username, role_full):
    """Return appropriate object based on role string in users.txt"""
    if "/" in role_full:
        role, sub_role = role_full.split("/", 1)
    else:
        role, sub_role = role_full, None

    if role == "Admin":
        return Admin(username, "Admin", None)
    if role == "Manager":
        return Manager(username, "Manager", None)
    if role == "Developer":
        return Developer(username, "Developer", sub_role)
    if role == "Intern":
        return Intern(username, "Intern", None)
    if role == "HR":
        return HR(username, "HR", None)
    # default: generic employee
    return Employee(username, role, sub_role)


def login_prompt():
    users = read_users()
    clear_screen()
    print("Welcome — Login screen")
    username = input("Username: ").strip()
    if username not in users:
        print("Unknown user.")
        pause()
        return None
    role, password = users[username]
    pwd = getpass.getpass("Password: ")
    if pwd != password:
        print("Incorrect password.")
        pause()
        return None
    # instantiate appropriate subclass
    emp = create_employee_object(username, role)
    return emp


def main():
    ensure_dirs()
    while True:
        clear_screen()
        print("=== Employee Workflow Console ===")
        print("1) Login")
        print("2) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            emp = login_prompt()
            if emp:
                emp.menu()
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()
