# Simon Says Memory Game

## Overview

This Python script implements the classic "Simon Says" memory game. Simon generates a random sequence of 10 colors, and the player must repeat the sequence. The colors are displayed one at a time with a 1-second delay between each, and the console is cleared after a 2-second pause before the player is asked to repeat the sequence.

## How to Play

1. Run the script.
2. Simon will display a sequence of 10 colors: R (Red), G (Green), B (Blue), and Y (Yellow).
3. Watch carefully as each color is displayed with a 1-second delay.
4. After all colors are displayed, the console will be cleared.
5. Enter the sequence you remember in the same order, using spaces between colors (e.g., `R G B Y`).
6. The game will compare the two sequences using a two-pointer approach and calculate your score based on how many correct matches you made.
7. The score is displayed, along with the original sequence.

## Features

- **Real-time color display**: The game shows each color with a 1-second delay, giving the player a chance to memorize the sequence.
- **Two-pointer comparison**: The scoring system compares the user's input with Simon's sequence without stopping on the first mismatch, allowing the player to earn points for every correct match.
- **Clear console**: The console is cleared after displaying the sequence, making it more challenging for the player to recall the colors.

## Requirements

- Python 3.x

## How to Run

1. Clone this repository or download the `simon_says.py` file.
2. Run the script: `python simon_says.py`
3. Follow the on-screen instructions to play.

## File Structure

- `simon_says.py`: The main script for the game.
- `README.md`: This documentation file.
