# Hangman with Hints

A classic Hangman word-guessing game with an integrated hint system, implemented in Python.

## Description

This is a console-based implementation of the classic Hangman game. Players try to guess a word letter by letter before running out of attempts. The game includes a unique hint feature that provides contextual clues about the word being guessed.

## Features

- **Word Bank**: 15 programming and computer-related words with corresponding hints
- **Hint System**: Players can request one hint per game to get a clue about the word
- **ASCII Art Display**: Visual representation of the hangman that updates with each incorrect guess
- **Input Validation**: Ensures players enter valid single letters
- **Game Statistics**: Tracks guessed letters and remaining attempts
- **Play Again Option**: Allows multiple rounds without restarting the program
- **User-Friendly Interface**: Clear visual feedback and game state information

## How to Play

1. Run the program:
   ```bash
   python hangman_with_hints.py
   ```

2. The game will randomly select a word from the word bank

3. Guess letters one at a time by typing them when prompted

4. Type 'hint' at any time to receive a clue about the word (one hint per game)

5. Type 'quit' to exit the current game

6. Win by guessing all letters correctly before making 6 incorrect guesses

7. After each game, you'll be asked if you want to play again

## Game Rules

- You have 6 incorrect guesses before the game ends
- Each correct guess reveals all instances of that letter in the word
- You can use one hint per game
- Letters can only be guessed once
- Only single letters are accepted as valid input

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Sample Gameplay

```
==================================================
Welcome to Hangman with Hints!
==================================================

       --------
       |      |
       |
       |
       |
       |
    --------

Word: _ _ _ _ _ _
Incorrect guesses remaining: 6
Guessed letters: None

Enter a letter, 'hint' for a hint, or 'quit' to exit: hint

Hint: A popular programming language named after a comedy group

Enter a letter, 'hint' for a hint, or 'quit' to exit: p

Good guess! 'p' is in the word.
```

## Code Structure

- `WORD_BANK`: Dictionary containing words and their corresponding hints
- `HangmanGame` class: Main game logic and state management
  - `choose_word()`: Randomly selects a word from the bank
  - `display_word()`: Shows the word with guessed letters revealed
  - `display_hangman()`: Renders ASCII art based on incorrect guesses
  - `get_hint()`: Provides the hint for the current word
  - `make_guess()`: Processes player's letter guesses
  - `is_won()`: Checks if the player has won
  - `is_lost()`: Checks if the player has lost
  - `play()`: Main game loop
- `main()`: Entry point with play-again functionality

## Contributing

This project is part of the 100 Lines of Python Code initiative. Feel free to suggest improvements or additional features!

## Related Issue

This implementation addresses issue #868 in the 100LinesOfPythonCode repository.

## License

Open source - feel free to use and modify as needed.
