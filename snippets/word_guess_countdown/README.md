# Word Guess Countdown

An interactive word guessing game with a countdown timer! Race against time to guess the hidden word before the clock runs out.

## Description

Word Guess Countdown is a terminal-based word guessing game where players must guess a randomly selected word letter by letter within 60 seconds. The game features a hint system, wrong guess tracking, and engaging visual feedback with emojis.

## Features

- 🎮 **Interactive Gameplay**: Guess letters one at a time to reveal the hidden word
- ⏱️ **60-Second Timer**: Race against the clock to complete the word
- 💡 **Hint System**: Get up to 2 hints per game to reveal random letters
- ❌ **Wrong Guess Limit**: Maximum of 10 wrong guesses allowed
- 🎨 **Visual Feedback**: Emoji-based feedback for correct/incorrect guesses
- 🔄 **Replay Option**: Play multiple rounds without restarting the program
- 📚 **Word Bank**: 20 programming-related words to guess

## How to Play

1. Run the script:
   ```bash
   python word_guess_countdown.py
   ```

2. The game will display:
   - The hidden word (shown as underscores)
   - Time remaining
   - Number of wrong guesses
   - Previously guessed letters
   - Available hints

3. Enter a single letter to guess, or:
   - Type `hint` to reveal a random letter (limited to 2 hints)
   - Type `quit` to exit the game

4. Continue guessing until:
   - ✅ You complete the word (WIN!)
   - ⏰ Time runs out (LOSE)
   - ❌ You reach 10 wrong guesses (LOSE)

5. After each game, choose whether to play again

## Game Rules

- Each letter can only be guessed once
- Only single alphabetic characters are accepted
- Time limit: 60 seconds per game
- Wrong guess limit: 10 incorrect guesses
- Hints available: 2 per game

## Example Output

```
==================================================
   WORD GUESS COUNTDOWN GAME
==================================================

Guess the word before time runs out!
You have 60 seconds and 10 wrong guesses allowed.

--------------------------------------------------
Word: _ _ _ _ _ _
Time remaining: 58s | Wrong guesses: 0/10
Guessed letters: None
Hints available: 2

Enter a letter (or 'hint' for help, 'quit' to exit): p
✅ Correct! 'P' is in the word!

--------------------------------------------------
Word: p _ _ _ _ _
Time remaining: 55s | Wrong guesses: 0/10
Guessed letters: p
Hints available: 2
```

## Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## Code Statistics

- Total lines: 98 (well under the 100-line requirement)
- Functions: 3
- Word bank: 20 programming-related terms

## Author

Contribution to [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode)

## License

This project is part of the 100LinesOfPythonCode repository.
