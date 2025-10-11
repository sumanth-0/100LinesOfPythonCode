#!/usr/bin/env python3
"""Personal Finance Debt Payoff Calculator & Strategy Planner"""

from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Debt:
    name: str
    balance: float
    interest_rate: float
    min_payment: float

def calculate_payoff(debt: Debt, monthly_payment: float) -> Tuple[int, float]:
    """Calculate months to payoff and total interest paid."""
    balance, rate = debt.balance, debt.interest_rate / 1200
    months, total_interest = 0, 0
    while balance > 0 and months < 1200:
        interest = balance * rate
        principal = min(monthly_payment - interest, balance)
        if principal <= 0: return -1, -1
        total_interest += interest
        balance -= principal
        months += 1
    return months, total_interest

def avalanche_strategy(debts: List[Debt], extra_payment: float) -> List[Dict]:
    """Debt Avalanche: Pay highest interest rate first."""
    debts = sorted(debts, key=lambda d: d.interest_rate, reverse=True)
    return execute_strategy(debts, extra_payment)

def snowball_strategy(debts: List[Debt], extra_payment: float) -> List[Dict]:
    """Debt Snowball: Pay lowest balance first."""
    debts = sorted(debts, key=lambda d: d.balance)
    return execute_strategy(debts, extra_payment)

def execute_strategy(debts: List[Debt], extra: float) -> List[Dict]:
    """Execute debt payoff strategy."""
    debts = [Debt(d.name, d.balance, d.interest_rate, d.min_payment) for d in debts]
    results, month = [], 0
    while debts and month < 1200:
        month += 1
        remaining_extra = extra
        for debt in debts:
            rate = debt.interest_rate / 1200
            interest = debt.balance * rate
            payment = debt.min_payment + (remaining_extra if debt == debts[0] else 0)
            principal = min(payment - interest, debt.balance)
            debt.balance -= principal
            remaining_extra = max(0, remaining_extra - (payment - debt.min_payment))
            if debt.balance <= 0:
                results.append({'name': debt.name, 'month': month, 'interest': 0})
        debts = [d for d in debts if d.balance > 0]
    return results

def main():
    print("Personal Finance Debt Payoff Calculator\n" + "="*50)
    debts = []
    n = int(input("Number of debts: "))
    for i in range(n):
        print(f"\nDebt #{i+1}:")
        name = input("  Name: ")
        balance = float(input("  Balance: $"))
        rate = float(input("  Interest Rate (%): "))
        min_pay = float(input("  Minimum Payment: $"))
        debts.append(Debt(name, balance, rate, min_pay))
    
    extra = float(input("\nExtra monthly payment: $"))
    
    print("\n" + "="*50)
    print("AVALANCHE STRATEGY (Highest Interest First)")
    print("="*50)
    avalanche = avalanche_strategy(debts, extra)
    total_months = max(d['month'] for d in avalanche)
    print(f"Total payoff time: {total_months} months ({total_months//12}y {total_months%12}m)")
    for debt in avalanche:
        print(f"  {debt['name']}: Paid off in month {debt['month']}")
    
    print("\n" + "="*50)
    print("SNOWBALL STRATEGY (Lowest Balance First)")
    print("="*50)
    snowball = snowball_strategy(debts, extra)
    total_months = max(d['month'] for d in snowball)
    print(f"Total payoff time: {total_months} months ({total_months//12}y {total_months%12}m)")
    for debt in snowball:
        print(f"  {debt['name']}: Paid off in month {debt['month']}")
    
    print("\n" + "="*50)
    print("Recommendation: Avalanche saves more on interest, Snowball provides quick wins.")

if __name__ == "__main__":
    main()
