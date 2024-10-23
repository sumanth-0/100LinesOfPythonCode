import random

# Function to generate an arithmetic progression puzzle
def generate_arithmetic_puzzle():
    start = random.randint(1, 10)  # Random start number
    diff = random.randint(2, 10)   # Random difference between numbers
    length = random.randint(4, 7)  # Length of the progression

    sequence = [start + i * diff for i in range(length)]
    
    # Hide the last number for the user to guess
    puzzle = sequence[:-1] + ['?']
    answer = sequence[-1]
    
    return puzzle, answer

# Function to display the puzzle and check the answer
def play_puzzle():
    puzzle, answer = generate_arithmetic_puzzle()
    
    # Display the puzzle
    print("Solve the puzzle:")
    print("Sequence:", puzzle)
    
    # User input
    user_answer = int(input("Enter the missing number: "))
    
    # Check the answer
    if user_answer == answer:
        print("Correct! The answer is", answer)
    else:
        print(f"Wrong! The correct answer was {answer}.")

# Main function to run the puzzle game
def main():
    print("Welcome to the Math Puzzle Generator!")
    
    while True:
        play_puzzle()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
