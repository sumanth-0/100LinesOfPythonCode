import tkinter as tk
import random

# --- Main Application Class ---
class BinarySearchGame:
    def __init__(self, root):
        """Initializes the main GUI window and all its widgets."""
        self.root = root
        self.root.title("Binary Search Game")
        self.root.geometry("350x250") # Set window size

        # --- Create and Pack GUI Widgets ---

        # 1. Instruction Label: Tells the user the rules
        self.instruction_label = tk.Label(
            root, 
            text="I'm thinking of a number between 1 and 100.\n"
                 "You have 7 guesses to find it (using binary search!)",
            font=("Arial", 10),
            pady=10
        )
        self.instruction_label.pack()

        # 2. Guesses Remaining Label: Shows remaining attempts
        self.guess_label = tk.Label(root, text="Guesses remaining: 7", font=("Arial", 12, "bold"))
        self.guess_label.pack()

        # 3. Hint/Feedback Label: Gives "too high/low" hints
        self.hint_label = tk.Label(root, text="Make your first guess.", font=("Arial", 10, "italic"), fg="blue")
        self.hint_label.pack()

        # 4. User Input Entry Box
        self.entry = tk.Entry(root, width=10, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.focus_set() # Start with the cursor in the entry box

        # 5. Guess Button: Calls the check_guess function
        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        # 6. Reset Button: Calls the reset_game function
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=5)

        # Start the first game
        self.reset_game()

    def reset_game(self):
        """Resets the game to a new, fresh state."""
        # Pick a new secret number
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 7 # Max guesses for binary search on 1-100 is 7 (2^7 > 100)

        # Reset all labels and buttons to their starting state
        self.hint_label.config(text="New game started. Make your guess.", fg="blue")
        self.guess_label.config(text=f"Guesses remaining: {self.guesses_left}")
        self.entry.delete(0, tk.END) # Clear the entry box
        self.guess_button.config(state=tk.NORMAL) # Re-enable the guess button
        self.entry.config(state=tk.NORMAL) # Re-enable the entry box

    def check_guess(self):
        """Runs every time the user clicks the 'Guess' button."""
        try:
            # Get the guess from the entry box and convert to an integer
            guess = int(self.entry.get())
        except ValueError:
            # Handle bad input (e.g., "abc")
            self.hint_label.config(text="That's not a number! Try again.", fg="red")
            return # Stop the function here

        # A valid guess was made
        self.guesses_left -= 1
        self.guess_label.config(text=f"Guesses remaining: {self.guesses_left}")
        self.entry.delete(0, tk.END) # Clear the box for the next guess

        # --- Check Win/Loss/Hint Conditions ---
        if guess == self.secret_number:
            # --- WIN ---
            self.hint_label.config(text=f"You got it! The number was {self.secret_number}!", fg="green")
            self.guess_button.config(state=tk.DISABLED) # Disable button
            self.entry.config(state=tk.DISABLED) # Disable entry
        elif self.guesses_left == 0:
            # --- LOSE ---
            self.hint_label.config(text=f"You lost! The number was {self.secret_number}.", fg="red")
            self.guess_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)
        elif guess < self.secret_number:
            # --- HINT: TOO LOW ---
            self.hint_label.config(text=f"Your guess {guess} is too LOW.", fg="orange")
        elif guess > self.secret_number:
            # --- HINT: TOO HIGH ---
            self.hint_label.config(text=f"Your guess {guess} is too HIGH.", fg="orange")

# --- Main execution: Runs the program ---
if __name__ == "__main__":
    main_root = tk.Tk()           # Create the main window
    app = BinarySearchGame(main_root) # Create our game app instance
    main_root.mainloop()          # Start the GUI event loop