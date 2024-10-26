class FinanceLogger:
    def __init__(self):
        self.expenses = []
        self.income = []

    def log_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def log_income(self, amount, description):
        self.income.append({"amount": amount, "description": description})

    def monthly_totals(self):
        total_income = sum(item["amount"] for item in self.income)
        total_expenses = sum(item["amount"] for item in self.expenses)
        return total_income, total_expenses, total_income - total_expenses

def main():
    logger = FinanceLogger()

    while True:
        action = input("Log (E)xpense, (I)ncome, or (Q)uit: ").lower()
        if action == 'e':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            logger.log_expense(amount, description)
        elif action == 'i':
            amount = float(input("Enter income amount: "))
            description = input("Enter income description: ")
            logger.log_income(amount, description)
        elif action == 'q':
            break

        income, expenses, balance = logger.monthly_totals()
        print(f"\nTotal Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Balance: ${balance:.2f}\n")

if __name__ == "__main__":
    main()
