# Color Guess Game 🎨

An interactive command-line game where players guess color names based on their RGB values.

## Description

The Color Guess Game challenges players to identify colors from their RGB (Red, Green, Blue) values. The game provides hints based on the RGB composition and tracks your score throughout multiple rounds.

## Features

- 🎯 **15 Different Colors**: Includes common colors like red, blue, green, yellow, purple, and more
- 💡 **Smart Hints**: Provides helpful hints based on RGB value patterns
- 📊 **Score Tracking**: Keeps track of your correct guesses and overall accuracy
- ✅ **Instant Feedback**: Get immediate feedback on whether your guess was correct
- 🎮 **Multiple Rounds**: Play as many rounds as you like

## How to Play

1. Run the script:
   ```bash
   python color_guess_game.py
   ```

2. The game will display RGB values (e.g., RGB: (255, 0, 0))

3. You'll receive a hint about the color composition

4. Type your guess (e.g., "red", "blue", "green")

5. Get instant feedback on your answer

6. Choose to play another round or quit

## Available Colors

The game includes these colors:
- red, green, blue
- yellow, purple, orange
- pink, brown, black, white
- gray, cyan, magenta
- lime, navy

## Example Gameplay

```
==================================================
    🎨 WELCOME TO THE COLOR GUESS GAME! 🎨
==================================================

Rules:
- I'll show you RGB values
- You guess the color name
- Get points for correct answers
- Type 'quit' to exit

🎯 RGB: (255, 165, 0)
💡 Hint: high red

Your guess: orange
✅ Correct! Well done!

📊 Score: 1/1
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Code Structure

- `COLORS`: Dictionary mapping color names to RGB tuples
- `display_welcome()`: Shows game instructions
- `get_color_hint()`: Generates hints based on RGB values
- `play_round()`: Handles a single game round
- `main()`: Main game loop with score tracking

## Learning Outcomes

- Understanding RGB color values
- Color recognition and composition
- Improving color theory knowledge
- Fun way to memorize common color codes

## Contributing

Feel free to enhance the game by:
- Adding more colors
- Implementing difficulty levels
- Adding time challenges
- Creating a GUI version

## License

This project is part of the 100LinesOfPythonCode repository.

---

**Enjoy the game and happy color guessing!** 🌈
