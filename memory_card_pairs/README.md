# Memory Card Pairs

A terminal-based card matching game where players flip cards to find matching pairs.

## Description

This is a fun and interactive memory card game that runs in the terminal. Players are presented with a grid of face-down cards and must flip them two at a time to find matching pairs. The game tracks the number of turns and attempts taken to complete the game.

## Features

- 🎮 Interactive terminal-based gameplay
- 🎴 8 pairs of cards (16 total) with colorful emoji symbols
- 📊 Turn and attempt tracking
- ✅ Visual feedback for matched pairs
- 🎯 Clear grid layout with numbered positions
- 🚪 Option to quit at any time
- 🏆 Victory screen with final statistics

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository
2. Navigate to the memory_card_pairs folder

```bash
cd memory_card_pairs
```

## Usage

Run the game using Python:

```bash
python memory_card_pairs.py
```

or

```bash
python3 memory_card_pairs.py
```

## How to Play

1. The game starts with a 4x4 grid of face-down cards (shown as `[?]`)
2. Cards are numbered from 1 to 16
3. Enter the number of the first card you want to flip
4. Enter the number of the second card you want to flip
5. If the cards match, they will be marked as matched (shown as `✓`)
6. If the cards don't match, try to remember their positions for your next turn
7. Continue until all pairs are matched
8. Type 'quit' at any time to exit the game

## Game Statistics

The game tracks:
- **Turns**: The number of complete turns (two card flips per turn)
- **Attempts**: Total number of matching attempts made

## Example Gameplay

```
==================================================
   MEMORY CARD PAIRS GAME
==================================================
Turns: 0 | Attempts: 0
==================================================

  1    2    3    4  
 [?]  [?]  [?]  [?] 

  5    6    7    8  
 [?]  [?]  [?]  [?] 

  9   10   11   12  
 [?]  [?]  [?]  [?] 

 13   14   15   16  
 [?]  [?]  [?]  [?] 

Select the first card:
```

## Contributing

This project is part of the 100 Lines of Python Code challenge. Feel free to fork, modify, and submit pull requests!

## License

This project is open source and available under the MIT License.

## Issue Reference

This implementation addresses issue #870 - Memory Card Pairs game with turn tracking.
