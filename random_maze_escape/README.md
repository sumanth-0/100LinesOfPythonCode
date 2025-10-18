# Random Maze Escape

## Description
A Python implementation of a random maze generator with an automatic pathfinder. The program generates a mini maze with ASCII walls and finds the shortest path from start to exit using the Breadth-First Search (BFS) algorithm.

## Features
- **Random Maze Generation**: Creates unique mazes using recursive backtracking algorithm
- **ASCII Visualization**: Displays mazes using simple text characters
- **Shortest Path Finding**: Uses BFS to find the optimal path from start to exit
- **Path Visualization**: Shows the solution path marked with dots

## Requirements
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## How to Run
```bash
python random_maze_escape.py
```

## Output
The program displays:
1. Original maze with start (S) and exit (E) positions
2. The length of the shortest path
3. Maze with the solution path marked with dots (.)
4. Total number of steps required to escape

## Maze Symbols
- `#` : Wall
- `S` : Start position
- `E` : Exit position
- `.` : Path to the exit
- ` ` : Empty walkable space

## Example Output
```
=== Random Maze Escape ===

Generating maze...

Original Maze (S=Start, E=Exit):
###############
#S            #
### ######### #
#   #       # #
# ### ##### # #
#   #     # # #
### ##### # # #
#       # # # #
####### # # # #
#       #   # #
# ######### # #
#           # #
############# E
###############

Path found! Length: 45 steps
```

## Algorithm
- **Maze Generation**: Recursive backtracking (DFS-based)
- **Pathfinding**: Breadth-First Search (BFS)

## Author
Contribution to 100LinesOfPythonCode repository

## License
This project follows the license of the parent repository.
