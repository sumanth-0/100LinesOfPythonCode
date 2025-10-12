# Rock-Paper-Scissors-Lizard-Spock

An expanded version of the classic Rock-Paper-Scissors game with five choices and complete winner logic, popularized by The Big Bang Theory.

## Features

- **Five Choices**: Rock, Paper, Scissors, Lizard, Spock
- **Complete Rules**: All 10 winning combinations implemented
- **Action Descriptions**: Shows how each choice beats another
- **Score Tracking**: Keeps track of wins, losses, and ties
- **Flexible Input**: Accept numbers (1-5) or choice names
- **Multiple Rounds**: Play as many rounds as desired

## Game Rules

Each choice defeats exactly two others:

- **Rock** crushes Lizard and crushes Scissors
- **Paper** covers Rock and disproves Spock
- **Scissors** cuts Paper and decapitates Lizard
- **Lizard** poisons Spock and eats Paper
- **Spock** smashes Scissors and vaporizes Rock

## Usage

```bash
python rpsls_game.py
```

## Example Game

```
Rock-Paper-Scissors-Lizard-Spock
===================================

Choices:
1. Rock
2. Paper
3. Scissors
4. Lizard
5. Spock

Enter your choice (1-5 or name): spock

You chose: Spock
Computer chose: Scissors

You win! Spock smashes Scissors

Score - You: 1, Computer: 0, Ties: 0

Play again? (y/n): n

Final Score:
You: 1
Computer: 0
Ties: 0
You won overall!
```

## Input Options

| Input | Choice |
|-------|--------|
| `1` or `rock` | Rock |
| `2` or `paper` | Paper |
| `3` or `scissors` | Scissors |
| `4` or `lizard` | Lizard |
| `5` or `spock` | Spock |

## Victory Conditions

The game uses the complete RPSLS rule set where each choice has exactly two choices it defeats:

```
Rock > Lizard, Scissors
Paper > Rock, Spock
Scissors > Paper, Lizard
Lizard > Spock, Paper
Spock > Scissors, Rock
```

## Requirements

- Python 3.6+
- No external dependencies

## Game Flow

1. Display available choices
2. Get player input (number or name)
3. Generate random computer choice
4. Determine winner using rules
5. Show action description
6. Update scores
7. Ask to play again

## Author

Created for issue #783 - 100 Lines of Python Code Project