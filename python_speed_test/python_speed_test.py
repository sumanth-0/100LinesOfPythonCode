"""
Python Speed Test
Measure how fast your computer executes loops or arithmetic operations
"""

import time

def test_loop(n=10**6):
    start = time.time()
    total = 0
    for i in range(n):
        total += i
    end = time.time()
    print(f"Loop Test: Summed 0 to {n-1} in {end-start:.6f} seconds")

def test_arithmetic(n=10**6):
    start = time.time()
    result = 1.0
    for i in range(1, n):
        result *= 1.000001
        result /= 1.000001
    end = time.time()
    print(f"Arithmetic Test: Performed {n} multiplications/divisions in {end-start:.6f} seconds")

def main():
    print("\n⚡ Python Speed Test ⚡")
    while True:
        print("\nMenu:")
        print("1️⃣  Test Loop Speed")
        print("2️⃣  Test Arithmetic Speed")
        print("3️⃣  Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            test_loop()
        elif choice == "2":
            test_arithmetic()
        elif choice == "3":
            print("Goodbye! 🏃💨")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
