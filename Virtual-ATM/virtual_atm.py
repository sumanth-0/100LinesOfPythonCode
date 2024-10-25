class VirtualATM:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def main():
    atm = VirtualATM()
    while True:
        print("\n--- Virtual ATM ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '3':
            atm.check_balance()
        elif choice == '4':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
