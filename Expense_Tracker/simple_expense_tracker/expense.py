def add(l):
    total=0
    for i in l:
        total=total+i
    return total
a=int(input("Enter How Many Category of Expenses are there.."))
final=0
number=1
print("Welcome to Expense Tracker")
for j in range(a): 
    Category=input(f"Enter Your {number} Category for expense")
    z=list(map(int,input("Enter the Expensese with a space between them").split()))
    print(f"Your Total expense for {Category} =  {add(z)}")
    final=final+add(z)
    number+=1
print(f"Your total final Expense is {final}")