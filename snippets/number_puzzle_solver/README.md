# Number Puzzle Solver

A Python implementation of the classic 8-puzzle (3x3 sliding puzzle) solver using the A* search algorithm.

## Description

The Number Puzzle Solver is a program that solves the classic sliding tile puzzle. The puzzle consists of a 3x3 grid with tiles numbered 1-8 and one empty space. The goal is to rearrange the tiles from a given initial state to reach the goal state where tiles are in order from 1 to 8.

## Features

- **A* Search Algorithm**: Uses the efficient A* algorithm for optimal solution finding
- **Manhattan Distance Heuristic**: Implements Manhattan distance for accurate state evaluation
- **Step-by-Step Solution**: Displays each move in the solution path
- **Optimal Solutions**: Finds the shortest path from initial state to goal state

## Goal State

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
```

Where `0` represents the empty space.

## Usage

```python
python number_puzzle_solver.py
```

### Custom Puzzle

You can modify the initial puzzle state in the code:

```python
puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = solve_puzzle(puzzle)
```

## Example Output

```
Initial State:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Solved in 2 moves!

Step 0:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 1:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 2:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
```

## Algorithm

The solver uses the **A* search algorithm** with the following components:

1. **State Representation**: Each puzzle state is represented as a 2D list
2. **Heuristic Function**: Manhattan distance calculates the sum of distances each tile needs to move
3. **Priority Queue**: States are explored in order of `f(n) = g(n) + h(n)` where:
   - `g(n)` = number of moves from start
   - `h(n)` = Manhattan distance heuristic
4. **Neighbor Generation**: Generates valid moves (up, down, left, right)

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Author

Contribution to 100LinesOfPythonCode repository

## License

This project follows the license of the parent repository.
