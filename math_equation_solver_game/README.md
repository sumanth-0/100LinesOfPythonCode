# Math Equation Solver Game

A fun and educational command-line game that challenges players to solve randomly generated math equations with varying difficulty levels.

## Description

Math Equation Solver Game is an interactive Python game that tests your mathematical skills across different difficulty levels. Players solve equations against the clock, earning points based on accuracy and speed. The game includes three difficulty modes with progressively challenging problems.

## Features

- **Three Difficulty Levels:**
  - Easy: Addition and subtraction (numbers 1-10)
  - Medium: Addition, subtraction, and multiplication (numbers 1-20)
  - Hard: All four operations including division (larger numbers)

- **Time-Based Scoring:** Faster answers earn more points
- **5 Rounds per Game:** Each game session includes 5 equation rounds
- **Immediate Feedback:** Get instant results showing correctness, time taken, and points earned
- **Score Tracking:** Final score displayed at the end of each game

## Requirements

- Python 3.6 or higher
- No external libraries required (uses only standard library modules)

## Installation

1. Clone this repository or download the `math_equation_solver_game.py` file
2. Navigate to the directory containing the file

```bash
cd math_equation_solver_game
```

## Usage

Run the game using Python:

```bash
python math_equation_solver_game.py
```

### How to Play

1. Select a difficulty level (1-3) from the main menu
2. Solve 5 randomly generated math equations
3. Enter your answer for each equation
4. Try to answer as quickly as possible for maximum points
5. View your final score at the end of the game
6. Choose to play again or quit

### Scoring System

- Maximum 10 points per correct answer
- Points decrease based on time taken (minimum 1 point per correct answer)
- Incorrect answers award 0 points
- Maximum possible score: 50 points (10 points × 5 rounds)

## Example Gameplay

```
==================================================
   MATH EQUATION SOLVER GAME
==================================================
1. Easy (Addition & Subtraction, 1-10)
2. Medium (Add, Sub, Mult, 1-20)
3. Hard (All operations, larger numbers)
4. Quit
==================================================

Select difficulty (1-4): 2

🎮 Starting Medium Mode - 5 rounds!

Round 1
Solve: 15 + 8
Your answer: 23
✓ Correct! Time: 2.5s | Points: +8

...

==================================================
Game Over! Final Score: 42/50
==================================================
```

## Code Structure

- `generate_equation(difficulty)`: Creates random math problems based on difficulty
- `display_menu()`: Shows the main menu with difficulty options
- `play_round(difficulty, round_num)`: Manages a single round of gameplay
- `play_game()`: Main game loop handling menu navigation and game sessions

## Educational Value

This game helps improve:
- Mental arithmetic skills
- Quick calculation abilities
- Mathematical confidence
- Time management under pressure

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available for educational purposes.

## Author

Created as part of the 100 Lines of Python Code project.

## Related Issues

Resolves issue #1166
