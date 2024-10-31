# Dungeon Treasure Hunt Game in Python

This Python script creates a simple interactive console-based game called **Dungeon Treasure Hunt**. The player navigates a dungeon represented by a 5x5 grid, aiming to collect treasures while avoiding traps.

## Game Features
1. **Grid Layout**: The dungeon is a 5x5 grid with random placements for treasures (marked as `T`) and traps (marked as `X`).
2. **Player Movement**: The player starts at the top-left corner (position `[0, 0]`) and moves using "W" (up), "S" (down), "A" (left), and "D" (right) keys.
3. **Score System**: 
   - **+10 points** for collecting a treasure.
   - **-5 points** for stepping on a trap.
4. **Winning and Losing**: 
   - **Win** by reaching 30 points.
   - **Lose** by dropping below -10 points.
5. **Console Display**: Each move updates the grid to reflect the player's position and status.

## Code Explanation

### 1. Initialize Variables and Symbols
The script begins by defining constants and symbols:
- `GRID_SIZE` determines the grid size.
- Symbols are defined for the **player**, **treasures**, **traps**, and **empty cells**.

### 2. Generating the Dungeon Grid
The function `generate_grid()` creates the 5x5 grid and places:
- **Treasures** (3–6 random positions) marked with `T`
- **Traps** (2–4 random positions) marked with `X`
- **Player** at the top-left corner.

### 3. Displaying the Grid
The `display_grid()` function visually represents the grid in the console, showing treasures, traps, and the player’s position.

### 4. Moving the Player
The `move_player()` function updates the player’s position based on the input direction:
- Moves are limited to within the grid bounds.
- If a **treasure** is found, points are added; if a **trap** is hit, points are subtracted.

### 5. Main Game Loop
The `play_game()` function starts the game loop:
- It displays the grid and prompts the player for a move.
- The player can move using "W", "A", "S", or "D" or quit with "Q".
- The game continues until the player either wins by collecting enough points or loses by hitting too many traps.

