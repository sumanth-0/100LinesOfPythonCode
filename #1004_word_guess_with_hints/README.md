# Word Guess with Hints

## Description
A fun word guessing game that provides helpful hints to make guessing easier and more engaging!

## Features
- 🎮 Interactive word guessing gameplay
- 💡 Synonym hints for each word
- 🔤 First letter hints available
- 📊 Track your guesses and progress
- 🔄 Play multiple rounds
- 15 different words with multiple synonyms each

## How to Play
1. Run the script
2. The game will display underscores representing each letter of the hidden word
3. Guess letters one at a time
4. Type 'hint' to get a synonym hint
5. Type 'first' to reveal the first letter
6. You have 7 incorrect guesses before game over
7. Win by guessing all letters in the word!

## Installation
No external dependencies required! Uses only Python standard library.

```bash
python word_guess_with_hints.py
```

## Usage Example
```
==================================================
   WORD GUESS WITH HINTS GAME
==================================================

Guess the word letter by letter!
Type 'hint' for a synonym hint
Type 'first' for the first letter hint

Word: _ _ _ _ _ _ _
Guesses left: 7
Guessed letters: None

Enter a letter (or 'hint'/'first'): hint
💡 Synonym hint: machine

Word: _ _ _ _ _ _ _
Guesses left: 7
Guessed letters: None

Enter a letter (or 'hint'/'first'): c
✓ Correct!
```

## Word Categories
The game includes words related to:
- Programming and technology
- Computer hardware and software
- Development concepts
- Technical terminology

## Game Mechanics
- **Synonym Hints**: Get a related word that describes the target word
- **First Letter Hint**: Reveals the first letter of the word
- **Guess Tracking**: See all letters you've already tried
- **Lives System**: 7 incorrect guesses allowed
- **Win Condition**: Guess all letters before running out of lives

## Contributing
This project is part of the #1004 issue for the 100LinesOfPythonCode repository.

## Author
Contribution to 100 Lines of Python Code Challenge

## License
Open source contribution - part of Hacktoberfest 2025
