# Color Guess Game 🎨

## Description
A fun and interactive Python game where players guess color names from RGB values. This game helps users learn about RGB color codes while testing their color recognition skills.

**Created for Issue #1165** - [Color Guess Game](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1165)

## Features
- 🎮 Interactive command-line gameplay
- 🌈 20 different colors with accurate RGB values
- 💡 Intelligent hints based on RGB composition
- 📊 Score tracking and statistics
- 🎯 10 rounds of color guessing fun
- ⏱️ Clean and intuitive user interface

## How to Play

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Running the Game

1. Navigate to the directory containing the file:
```bash
cd snippets/rgb_color_guesser
```

2. Run the game:
```bash
python color_guess_game.py
```

### Game Instructions
1. The game will display an RGB value (e.g., (255, 0, 0))
2. You'll receive a hint about the color composition
3. Type your guess for the color name
4. Get instant feedback on your answer
5. Play through 10 rounds
6. View your final statistics and accuracy

## Color List
The game includes 20 colors:
- Primary colors: red, green, blue
- Secondary colors: yellow, cyan, magenta
- Grayscale: white, black, gray
- Other colors: orange, purple, pink, brown, lime, navy, teal, maroon, olive, coral, turquoise

## Example Gameplay

```
==================================================
🎨 COLOR GUESS GAME 🎨
==================================================

Welcome! Guess the color name from RGB values.
You'll play 10 rounds.
RGB format: (Red, Green, Blue) - each 0-255
==================================================

--- Round 1/10 ---
RGB Value: (255, 0, 0)
Hint: High red content

Your guess: red
✓ Correct! 🎉

--- Round 2/10 ---
RGB Value: (255, 165, 0)
Hint: High red content

Your guess: orange
✓ Correct! 🎉
```

## Game Statistics
At the end of the game, you'll see:
- Total rounds played
- Number of correct guesses
- Accuracy percentage

## Educational Value
This game helps players:
- Understand RGB color model
- Learn common color RGB values
- Develop color recognition skills
- Practice associating numerical values with visual colors

## Code Structure
- `COLORS`: Dictionary mapping color names to RGB tuples
- `ColorGuessGame`: Main game class with all game logic
- `display_welcome()`: Shows game introduction
- `get_random_color()`: Selects random color from database
- `provide_hint()`: Generates hints based on RGB values
- `play_round()`: Handles single round gameplay
- `display_stats()`: Shows final statistics
- `main()`: Game entry point

## License
This project is part of the [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

## Contributing
Feel free to suggest improvements or report issues!

---

**Hacktoberfest 2025** | **Good First Issue** | **Python Game**
