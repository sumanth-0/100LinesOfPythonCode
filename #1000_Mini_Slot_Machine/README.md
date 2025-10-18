# Mini Slot Machine 🎰

## Description
A simple command-line slot machine simulator that provides an entertaining gambling experience with random symbol generation and payout logic.

## Features
- 🎲 Random symbol generation for three reels
- 💰 Dynamic payout system based on symbol matching
- 🎨 Animated spin effect
- 📊 Balance tracking system
- 🎯 Interactive betting mechanism
- 📋 Comprehensive paytable display

## Symbols & Payouts
The game features 7 different symbols with varying payout multipliers:
- 🍒 Cherry: 2x multiplier
- 🍋 Lemon: 3x multiplier
- 🍊 Orange: 4x multiplier
- 🍇 Grape: 5x multiplier
- 💎 Diamond: 10x multiplier
- 7️⃣ Lucky Seven: 20x multiplier
- ⭐ Star: 50x multiplier

## How to Play
1. Run the script: `python mini_slot_machine.py`
2. Starting balance is $100
3. Enter your bet amount (must be between $1 and your current balance)
4. Watch the reels spin!
5. Win conditions:
   - **Three matching symbols**: Win bet × symbol multiplier
   - **Two matching symbols**: Get your bet back
   - **No match**: Lose your bet

## Requirements
- Python 3.x
- No external libraries required (uses only built-in modules)

## Installation
```bash
git clone <repository-url>
cd #1000_Mini_Slot_Machine
python mini_slot_machine.py
```

## Game Rules
- You start with $100
- Minimum bet: $1
- Maximum bet: Your current balance
- Game continues until you run out of money or choose to quit
- Two matching symbols return your bet amount
- Three matching symbols multiply your bet by the symbol's value

## Example Gameplay
```
🎰  MINI SLOT MACHINE  🎰
Current Balance: $100

Enter bet amount (1-100): $10

Spinning...
┌─────┬─────┬─────┐
│  🍒  │  🍒  │  🍒  │
└─────┴─────┴─────┘

🎉 WINNER! You won $20!
New Balance: $110
```

## Code Structure
- `SlotMachine` class: Main game logic
- `display_header()`: Shows game title and balance
- `spin_reels()`: Generates random symbols
- `animate_spin()`: Creates spinning animation
- `calculate_payout()`: Determines winnings
- `display_result()`: Shows spin results
- `display_paytable()`: Shows payout information
- `get_bet()`: Handles user input for betting
- `play_round()`: Manages a single game round
- `play()`: Main game loop

## Contributing
This project is part of the 100 Lines of Python Code challenge. Feel free to fork and improve!

## Issue Reference
Implements: https://github.com/sumanth-0/100LinesOfPythonCode/issues/1000

## License
This project is open source and available under the MIT License.
