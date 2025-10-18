# Treasure Hunt Grid

## Description
An interactive treasure hunting game where players search for hidden treasure on a grid by guessing coordinates. The game provides proximity hints (Hot/Warm/Cold) and emoji indicators to guide players to the treasure location.

## Features
- Random treasure placement on a customizable grid
- Distance-based proximity hints
- Emoji indicators for guessed positions
- Score tracking based on number of attempts
- Input validation for coordinates

## How to Run
```bash
python treasure_hunt_grid.py
```

## Game Instructions
1. The game generates a grid and hides treasure at a random location
2. Enter coordinates in the format: row,column (e.g., 3,4)
3. The game will provide hints:
   - 🔥 **Hot!** - Very close to the treasure (distance ≤ 1)
   - 🌡️ **Warm!** - Getting closer (distance ≤ 2)
   - ❄️ **Cold!** - Far from the treasure
4. Keep guessing until you find the treasure!
5. Try to find it in as few attempts as possible

## Example
```
Welcome to Treasure Hunt!
Find the hidden treasure on a 5x5 grid.

Enter coordinates (row,column): 2,3
❄️ That's COLD! Try again.

Enter coordinates (row,column): 4,4
🌡️ Getting WARM! You're close!

Enter coordinates (row,column): 5,5
🔥 HOT! Very close!

Enter coordinates (row,column): 5,4
🎉 Congratulations! You found the treasure at (5, 4)!
You found it in 4 attempts!
```

## Author
Created as part of the 100 Lines of Python Code challenge.

## Issue Reference
Fixes #1163
