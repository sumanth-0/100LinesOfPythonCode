
# Expense Split Calculator for Group Trips

def calculate_expenses(expenses, participants):
    total_expense = sum(expenses)
    amount_per_person = total_expense / participants
    return amount_per_person

def main():
    participants = int(input("Enter the number of participants: "))
    expenses = []
    
    while True:
        expense = input("Enter an expense amount (or type 'done' to finish): ")
        if expense.lower() == 'done':
            break
        expenses.append(float(expense))
    
    amount_per_person = calculate_expenses(expenses, participants)
    print(f"Each person should contribute: ${amount_per_person:.2f}")

if __name__ == "__main__":
    main()
