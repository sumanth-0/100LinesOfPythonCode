# Command Line Tic-Tac-Toe AI

A command-line implementation of Tic-Tac-Toe with an unbeatable AI opponent.

## Description

This program implements a classic Tic-Tac-Toe game where you play against an AI opponent. The AI uses the minimax algorithm with alpha-beta pruning to make optimal moves, making it unbeatable. The best you can hope for is a tie!

## Features

- **Unbeatable AI**: Uses minimax algorithm with alpha-beta pruning
- **Simple Interface**: Easy-to-use command-line interface
- **Clear Board Display**: Visual representation of the game board
- **Input Validation**: Prevents invalid moves
- **Game Status**: Shows winner or tie at the end

## How to Play

1. Run the program:
   ```bash
   python command_line_tic_tac_toe_ai.py
   ```

2. You are X, and the AI is O

3. Enter your move by typing a number from 1-9 corresponding to the board position:
   ```
   1 | 2 | 3
   -----------
   4 | 5 | 6
   -----------
   7 | 8 | 9
   ```

4. The AI will automatically make its move after yours

5. The game continues until there's a winner or a tie

## Requirements

- Python 3.x
- No external libraries required

## Algorithm

The AI uses the minimax algorithm, a decision-making algorithm for turn-based games. It evaluates all possible game states and chooses the move that maximizes its chances of winning while minimizing the opponent's chances. Alpha-beta pruning is used to optimize the search by eliminating branches that cannot affect the final decision.

## Example Game

```
Welcome to Command Line Tic-Tac-Toe AI!
You are X, AI is O. Positions are 1-9.
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Your move (1-9): 5
AI is thinking...
AI chose position 1
...
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Issue Reference

This project was created to address issue #1168 in the 100LinesOfPythonCode repository.
