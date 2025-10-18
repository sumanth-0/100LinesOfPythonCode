# Word Scramble Challenge 🎮

A fun and interactive word scramble game where players guess scrambled words to earn points!

## Description

Word Scramble Challenge is an engaging Python game that tests your vocabulary and pattern recognition skills. The game scrambles random words and challenges you to unscramble them within a limited number of attempts. With multiple difficulty levels, a scoring system, and helpful hints, it provides an entertaining experience for players of all skill levels.

## Features

- **Three Difficulty Levels**:
  - **Easy**: 5-8 letter words (1x point multiplier)
  - **Medium**: 8-10 letter words (2x point multiplier)
  - **Hard**: 10+ letter words (3x point multiplier)

- **Scoring System**: Earn points based on:
  - Number of attempts used
  - Difficulty level selected
  - Faster correct guesses earn more points

- **Hint System**: Get up to 3 hints per game session
  - Hints reveal one letter at a time
  - Helps when you're stuck on difficult words

- **Interactive Gameplay**:
  - Clean, user-friendly command-line interface
  - Real-time feedback on guesses
  - Play multiple rounds in one session
  - Track your statistics

- **Game Statistics**: View your performance at the end:
  - Total score achieved
  - Number of words attempted
  - Hints used during gameplay
  - Difficulty level played

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/word_scramble_challenge
```

2. No additional installation needed - just run the script!

## Usage

### Basic Usage

Run the game using Python:

```bash
python word_scramble_challenge.py
```

or

```bash
python3 word_scramble_challenge.py
```

### Game Commands

During gameplay, you can use these commands:

- Type your guess to unscramble the word
- Type `hint` to reveal one letter (up to 3 hints total)
- Type `skip` to skip the current word
- Type `quit` to exit the game

### Example Gameplay

```
**************************************************
    WORD SCRAMBLE CHALLENGE    
**************************************************

Welcome! Unscramble words to earn points.
Correct guesses earn more points with fewer attempts!

==================================================
SELECT DIFFICULTY LEVEL
==================================================
1. Easy (5-8 letter words)
2. Medium (8-10 letter words)
3. Hard (10+ letter words)
==================================================

Enter your choice (1-3): 1

==================================================
ROUND 1
==================================================
Scrambled word: OTPYNH
Word length: 6 letters

Commands: 'hint' for a clue, 'skip' to skip, 'quit' to exit
==================================================

Your guess: python

🎉 Correct! You earned 30 points!
Total score: 30

Play another round? (yes/no): no

==================================================
GAME STATISTICS
==================================================
Total Score: 30
Words Attempted: 1
Hints Used: 0
Difficulty: EASY
==================================================

Thanks for playing! 🎮
```

## Code Structure

The game is built using object-oriented programming principles:

- **WordScrambleGame Class**: Main game class containing all game logic
  - `__init__()`: Initialize game settings and word lists
  - `scramble_word()`: Scramble letters of a word
  - `get_hint()`: Generate hints by revealing letters
  - `select_difficulty()`: Allow player to choose difficulty
  - `get_word_list()`: Return words based on difficulty
  - `play_round()`: Handle one round of gameplay
  - `display_stats()`: Show final game statistics
  - `run()`: Main game loop

## Educational Value

This project demonstrates:

- **Object-Oriented Programming (OOP)**: Class structure and methods
- **Type Hints**: Modern Python typing for better code clarity
- **Game Logic**: State management and user interaction
- **Data Structures**: Using lists and dictionaries effectively
- **User Input Handling**: Processing and validating user commands
- **Randomization**: Using Python's random module
- **String Manipulation**: Working with text and characters

## Contributing

Contributions are welcome! Feel free to:

- Add more word categories
- Implement additional difficulty levels
- Create new game modes
- Improve the scoring algorithm
- Enhance the user interface

Please follow the repository's contribution guidelines.

## License

This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

## Author

Contributed as part of Hacktoberfest 2025

## Related Issues

- Issue #1162: Word Scramble Challenge

## Acknowledgments

- Thanks to the 100LinesOfPythonCode community
- Inspired by classic word puzzle games
- Built for educational purposes and fun!

---

**Happy Scrambling!** 🎯✨
