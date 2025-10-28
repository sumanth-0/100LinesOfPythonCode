import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("--- Memory Sequence Test ---")
    print("A sequence of numbers will appear. Memorize it and type it back.")
    print("The sequence will get longer each round.")
    input("Press Enter to start...")
    
    sequence = []
    level = 1
    
    while True:
        clear_screen()
        sequence.append(random.randint(0, 9))
        
        print(f"Level {level} - Get ready...")
        time.sleep(1.5)
        
        print(' '.join(map(str, sequence)))
        time.sleep(len(sequence) * 0.7)
        
        clear_screen()
        
        user_input = input("Enter the sequence (separate with spaces): ")
        
        try:
            user_sequence = [int(num) for num in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers.")
            time.sleep(2)
            break
        
        if user_sequence == sequence:
            print(f"Correct! Get ready for Level {level + 1}.")
            level += 1
            time.sleep(2)
        else:
            print(f"Game Over! You reached Level {level}.")
            print(f"The correct sequence was: {' '.join(map(str, sequence))}")
            break
            
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()