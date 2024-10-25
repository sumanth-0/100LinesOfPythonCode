def guess_the_number():
    # Get the upper limit from the user
    N = int(input("Let's set an upper limit for the game! Enter a whole number above 1:"))
    print(f"Think of a number between 1 and {N}!")
    input("Press Enter when you are ready...")

    low, high = 1, N
    attempts = 0

    # Start the binary search loop
    while low <= high:
        attempts += 1
        # Calculate the midpoint guess
        guess = (low + high) // 2
        print(f"My guess is: {guess}")

        feedback = input("Is it higher, lower, or correct? (type 'higher' or 'lower' or 'correct'): ").strip().lower()

        if feedback == 'correct':
            print(f"Yay! I guessed your number in {attempts} attempts.")
            break
        elif feedback == 'higher':
            low = guess + 1
        elif feedback == 'lower':
            high = guess - 1
        else:
            print("Invalid input. Please respond with 'higher', 'lower', or 'correct'.")

    # Check if the search range is invalid
    if low > high:
        print("I couldn't find your number. Let's give it another shot!")

if __name__ == "__main__":
    guess_the_number()
