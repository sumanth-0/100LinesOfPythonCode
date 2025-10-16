# Word Scramble Game

A fun and interactive word scramble game where players unscramble letters to form the correct word.

## Description

This Python script implements a word scramble game where players are presented with scrambled letters from programming-related words. The game tracks your score, accuracy, and time played.

## Features

- **Interactive Gameplay**: Unscramble words to earn points
- **Hint System**: Get hints by revealing the first letter (costs 5 points)
- **Skip Functionality**: Skip difficult words without penalty
- **Score Tracking**: Earn 10 points for correct answers (5 points if hint was used)
- **Statistics**: View your accuracy, time played, and final score
- **20 Programming Words**: Includes words like "python", "algorithm", "debugging", and more

## How to Run

```bash
python word_scramble_game.py
```

## How to Play

1. The game will display a scrambled word
2. Type your answer and press Enter
3. Commands:
   - Type the unscrambled word to answer
   - Type `hint` for a hint (costs 5 points)
   - Type `skip` to skip the current word
   - Type `quit` to end the game

## Game Rules

- Correct answer without hint: **+10 points**
- Correct answer with hint: **+5 points**
- Using a hint: **-5 points**
- Skipping a word: **No penalty**

## Example Output

```
==================================================
   WELCOME TO WORD SCRAMBLE GAME!
==================================================

Instructions:
- Unscramble the letters to form the correct word
- Type your answer and press Enter
- Type 'hint' for a hint (costs 5 points)
- Type 'skip' to skip the current word
- Type 'quit' to end the game

Scrambled word: TPYHON
Word length: 6 letters
Your answer: python

✓ Correct! You earned 10 points!
Current score: 10
```

## Requirements

- Python 3.x
- No external libraries required (uses only standard library)

## Author

Contributed as part of the 100LinesOfPythonCode repository.

## License

This project is open source and available under the repository's license.
