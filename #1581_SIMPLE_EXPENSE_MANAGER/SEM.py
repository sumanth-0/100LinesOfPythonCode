import pandas as pd
from datetime import datetime
import os

MoneyDeposited = 5000
date_format = "%d-%m-%Y"
df = pd.read_excel('DEM.xlsx', index_col=False)
mainCategory = list(df["Categories"])
formatted_date = datetime.now().strftime("%b-%Y")
timestamp_file = "last_run.txt"

def getAmount(prompt):
    try:
        amt = float(input(prompt))
        if amt <= 0: raise ValueError("Amount must be > 0.")
        return amt
    except ValueError as e:
        print(e); return getAmount(prompt)

def getDate(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        return datetime.strptime(date_str, date_format).strftime(date_format)
    except ValueError:
        print("Use dd-mm-yyyy format."); return getDate(prompt, allow_default)

def getCategory():
    while True:
        ask = input("Enter Category (1-23): ")
        if ask.isdigit() and 1 <= int(ask) <= 23: return int(ask)
        print("Invalid. Enter number 1–23.")

def showCategories():
    for i, c in enumerate(df['Categories']): print(f"{i+1}) {c}")

def get_last_run_time():
    return open(timestamp_file).read().strip() if os.path.exists(timestamp_file) else "First run."

def update_last_run_time():
    open(timestamp_file, "w").write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def addExpense():
    showCategories(); c = getCategory()
    amt = getAmount(f"Enter amount for {mainCategory[c-1]}: ")
    df.loc[df["SrNO."] == c, formatted_date] += amt
    print(df[['Categories', formatted_date]])
    df.to_excel("DEM.xlsx", index=False)

def ViewExpense():
    try: m = int(input("Enter month (1-12): "))
    except ValueError: return ViewExpense()
    if not 1 <= m <= 12: return print("Invalid month.")
    d = datetime(datetime.now().year, m, 1).strftime("%b-%Y")
    total = df[d].sum()
    print(df[['Categories', d]])
    print(f"Total Expense: {total}\nBalance: {MoneyDeposited - total}")

def addLendedMoney():
    df1 = pd.read_csv('DEMLended.csv')
    n = input("Enter Name: ").title().strip()
    m = getAmount(f"Enter amount lent to {n}: ")
    showCategories(); c = getCategory()
    dt = getDate("Enter date (dd-mm-yyyy) or press Enter for today: ", True)
    new = pd.DataFrame({'Name':[n],'Money':[m],'Category':[mainCategory[c-1]],'Date':[dt]})
    df1 = pd.concat([df1, new], ignore_index=True)
    print(new); df1.to_csv('DEMLended.csv', index=False)

def viewLendedMoney():
    print(pd.read_csv('DEMLended.csv'))

def returnMoney():
    df3 = pd.read_csv('DEMLended.csv'); print(df3)
    while True:
        n = input("Enter Name: ").title().strip()
        if n in df3["Name"].values: break
    showCategories()
    while True:
        c = getCategory()
        s = df[df['Categories']==mainCategory[c-1]][formatted_date].sum()
        t = df3[(df3['Category']==mainCategory[c-1])&(df3["Name"]==n)]['Money'].sum()
        if t and s>t:
            money = input(f"Enter amount {n} returned (blank=full): ")
            money = float(money) if money else t
            df.loc[df['Categories']==mainCategory[c-1], formatted_date] = s - money
            df3.loc[(df3["Name"]==n)&(df3["Category"]==mainCategory[c-1]), "Money"] = t - money
            if t - money <= 0:
                df3 = df3[~((df3["Name"]==n)&(df3["Category"]==mainCategory[c-1]))]
            df3.to_csv('DEMLended.csv', index=False); df.to_excel('DEM.xlsx', index=False)
            break
        else: print("Incorrect category.")

if __name__ == '__main__':
    print("Last run:", get_last_run_time())
    while True:
        print("\n1.Add Expense  2.View Expense  3.Add Lended  4.View Lended  5.Returned  6.Exit")
        update_last_run_time()
        ch = input("Enter (1-6): ").strip()
        if ch=="1": addExpense()
        elif ch=="2": ViewExpense()
        elif ch=="3": addLendedMoney()
        elif ch=="4": viewLendedMoney()
        elif ch=="5": returnMoney()
        elif ch=="6": exit()
