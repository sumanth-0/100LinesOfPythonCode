import random
import time
import operator

def generate_equation(difficulty):
    """Generate a random math equation based on difficulty."""
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    if difficulty == 1:
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(['+', '-'])
    elif difficulty == 2:
        num1, num2 = random.randint(1, 20), random.randint(1, 20)
        op = random.choice(['+', '-', '*'])
    else:
        num1 = random.randint(10, 50)
        num2 = random.randint(1, 10)
        op = random.choice(['+', '-', '*', '/'])
        if op == '/':
            num1 = num2 * random.randint(1, 10)
    
    answer = ops[op](num1, num2)
    if op == '/':
        answer = int(answer)
    
    return f"{num1} {op} {num2}", answer

def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   MATH EQUATION SOLVER GAME")
    print("="*50)
    print("1. Easy (Addition & Subtraction, 1-10)")
    print("2. Medium (Add, Sub, Mult, 1-20)")
    print("3. Hard (All operations, larger numbers)")
    print("4. Quit")
    print("="*50)

def play_round(difficulty, round_num):
    """Play a single round of the game."""
    equation, correct_answer = generate_equation(difficulty)
    print(f"\nRound {round_num}")
    print(f"Solve: {equation}")
    
    start_time = time.time()
    try:
        user_answer = float(input("Your answer: "))
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        
        if abs(user_answer - correct_answer) < 0.01:
            points = max(10 - int(time_taken), 1)
            print(f"✓ Correct! Time: {time_taken}s | Points: +{points}")
            return points
        else:
            print(f"✗ Wrong! The correct answer was {correct_answer}")
            return 0
    except ValueError:
        print("✗ Invalid input! No points awarded.")
        return 0

def play_game():
    """Main game loop."""
    while True:
        display_menu()
        try:
            choice = input("\nSelect difficulty (1-4): ")
            
            if choice == '4':
                print("\nThanks for playing! Goodbye!")
                break
            
            difficulty = int(choice)
            if difficulty not in [1, 2, 3]:
                print("Invalid choice! Please select 1, 2, or 3.")
                continue
            
            total_score = 0
            rounds = 5
            
            print(f"\n🎮 Starting {['Easy', 'Medium', 'Hard'][difficulty-1]} Mode - {rounds} rounds!")
            
            for i in range(1, rounds + 1):
                score = play_round(difficulty, i)
                total_score += score
            
            print("\n" + "="*50)
            print(f"Game Over! Final Score: {total_score}/{rounds * 10}")
            print("="*50)
            
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    play_game()
