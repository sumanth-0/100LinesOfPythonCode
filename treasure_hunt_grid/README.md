# Treasure Hunt Grid Game 🏴‍☠️

## Description

An interactive treasure hunt grid game where players navigate through a grid-based map to collect hidden treasures while avoiding dangerous traps and obstacles. The objective is to collect all treasures and reach the exit with the highest score possible.

## Features

- **Grid-based gameplay**: Navigate through a customizable grid (5x5 to 20x20)
- **Interactive elements**: 
  - 💰 Treasures: Collect for points (10-50 points each)
  - 💥 Traps: Lose points when triggered (5-25 points lost)
  - 🧱 Obstacles: Block movement paths
  - 🚪 Exit: Escape point (bottom-right corner)
- **Player tracking**: 
  - Score system with bonus for efficiency
  - Move counter
  - Treasure collection progress
- **Visual interface**: Unicode emojis for enhanced visual appeal
- **Win condition**: Collect ALL treasures before reaching the exit
- **Move efficiency bonus**: Fewer moves = higher bonus score

## How to Run

```bash
python3 treasure_hunt_grid.py
```

## Gameplay Instructions

1. **Setup**: Choose your grid size (default: 10x10)
2. **Navigation**: Use WASD keys to move:
   - `W`: Move up
   - `A`: Move left  
   - `S`: Move down
   - `D`: Move right
   - `Q`: Quit game

3. **Objective**: 
   - Navigate the grid to collect all treasures (💰)
   - Avoid traps (💥) which reduce your score
   - Navigate around obstacles (🧱) which block movement
   - Reach the exit (🚪) after collecting ALL treasures

4. **Scoring**:
   - Treasures: +10 to +50 points (random)
   - Traps: -5 to -25 points (random) 
   - Efficiency bonus: +(100 - total_moves) points when winning

## Game Rules

- You start at the top-left corner (0,0)
- The exit is at the bottom-right corner
- You cannot move through obstacles
- You must collect ALL treasures before you can win at the exit
- Traps and treasures disappear after interaction
- Your goal is to maximize your score while minimizing moves

## Code Structure

- **TreasureHuntGrid class**: Main game logic and state management
- **Grid generation**: Random placement of treasures, traps, and obstacles
- **Player movement**: WASD controls with boundary checking
- **Visual display**: Clear terminal-based interface with emojis
- **Game statistics**: Score tracking and performance metrics

## Requirements

- Python 3.6 or higher
- Terminal/console that supports Unicode emojis
- No external dependencies required

## Example Game Session

```
🏴‍☠️  TREASURE HUNT GRID GAME  🏴‍☠️
==================================================
Score: 45 | Moves: 12 | Treasures: 2/5

Legend: P=Player, T=Treasure, X=Trap, #=Obstacle, E=Exit

    0  1  2  3  4  5  6  7  8  9 
 0 🤠 ⬜ 💰 🧱 ⬜ ⬜ 💥 ⬜ 💰 ⬜ 
 1 ⬜ 🧱 ⬜ ⬜ ⬜ 💰 ⬜ 🧱 ⬜ ⬜ 
 2 💰 ⬜ ⬜ 💥 ⬜ ⬜ ⬜ ⬜ ⬜ 🧱 
 3 ⬜ ⬜ 🧱 ⬜ ⬜ ⬜ 💥 ⬜ ⬜ ⬜ 
 4 ⬜ 💰 ⬜ ⬜ 🧱 ⬜ ⬜ ⬜ ⬜ 🚪 

📍 Controls: WASD (W=Up, A=Left, S=Down, D=Right), Q=Quit
```

## Contributing

This implementation was created for issue #1163 in the 100LinesOfPythonCode repository. The code follows Python best practices with:

- Type hints for better code readability
- Comprehensive docstrings
- Error handling and input validation
- Clean, modular structure
- 315+ lines of well-documented code

## Author

Implemented as part of the 100LinesOfPythonCode project contribution.

**Issue**: [#1163 - Treasure Hunt Grid](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1163)  
**Pull Request**: Adds treasure hunt grid game implementation
