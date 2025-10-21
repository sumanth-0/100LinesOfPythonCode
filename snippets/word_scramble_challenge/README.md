# Word Scramble Challenge

## Description
Word Scramble Challenge is an interactive command-line game where players unscramble words from various categories within a time limit. Test your vocabulary and speed in this fun and educational word puzzle game!

## Features
- **Multiple Categories**: Choose from animals, countries, fruits, and technology words
- **Timed Challenges**: 30 seconds per word to keep the excitement high
- **Scoring System**: Earn 10 points for each correct answer
- **Hint System**: Get hints for 3 points (reveals first and last letters)
- **Skip Option**: Skip difficult words if needed
- **Customizable Rounds**: Play 1-20 rounds per game session
- **Performance Statistics**: View accuracy and final score at the end

## Requirements
- Python 3.x
- No external dependencies required (uses only standard library)

## How to Run

1. Navigate to the word_scramble_challenge directory:
```bash
cd snippets/word_scramble_challenge
```

2. Run the game:
```bash
python word_scramble_challenge.py
```

3. Follow the on-screen instructions:
   - Choose the number of rounds (1-20)
   - Unscramble the displayed words
   - Type your answer and press Enter
   - Use 'hint' for help, 'skip' to pass, or 'quit' to exit

## Game Commands
- **Your answer**: Type the unscrambled word
- **hint**: Get a hint (costs 3 points)
- **skip**: Skip the current word
- **quit**: Exit the game

## Example Gameplay
```
==================================================
  WORD SCRAMBLE CHALLENGE
==================================================

Welcome to the Word Scramble Challenge!

Instructions:
- Unscramble the word within the time limit
- Each correct answer earns you 10 points
- Type 'hint' for a hint (costs 3 points)
- Type 'skip' to skip the current word
- Type 'quit' to exit the game
==================================================

How many rounds would you like to play? (1-20): 3

Round 1
Category: ANIMALS
Scrambled word: EHNPTALE
Word length: 8 letters

Time remaining: 30s
Your answer: elephant

✅ Correct! +10 points
Score: 10

Round 2
Category: FRUITS
Scrambled word: NAAANB
Word length: 6 letters

Time remaining: 30s
Your answer: hint

💡 Hint: b...a
Score: 7

Time remaining: 25s
Your answer: banana

✅ Correct! +10 points
Score: 17

Round 3
Category: COUNTRIES
Scrambled word: AANZILT
Word length: 8 letters

Time remaining: 30s
Your answer: skip

Skipped! The correct word was: TANZANIA

==================================================
  GAME OVER
==================================================

Rounds played: 3
Correct answers: 2
Final score: 17
Accuracy: 66.7%

Thanks for playing Word Scramble Challenge!
==================================================
```

## Code Structure
- **WordScrambleGame Class**: Main game logic and state management
- **Word Categories**: Organized dictionary of themed word lists
- **Scrambling Algorithm**: Ensures scrambled words differ from originals
- **Time Management**: 30-second countdown per round
- **Scoring System**: Points for correct answers, penalties for hints

## Contributing
This project is part of the 100 Lines of Python Code challenge. Feel free to fork and enhance!

## License
Open source - feel free to use and modify.

## Author
Created as a solution for Issue #1162 - Word Scramble Challenge

## Acknowledgments
Thanks to the 100LinesOfPythonCode repository for the inspiration and opportunity to contribute!
