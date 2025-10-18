# Dice Guess Challenge

A fun and interactive command-line game where you try to guess the number rolled on a dice!

## Description

Dice Guess Challenge is a simple yet engaging guessing game where:
- The computer rolls a virtual dice (1-6)
- You have 3 attempts to guess the correct number
- Earn points based on how quickly you guess correctly
- Try to beat your high score across multiple rounds

## Features

- 🎲 Random dice rolling (1-6)
- 🎯 3 attempts per round
- 📊 Score tracking system
- 🏆 High score tracking
- 💡 Helpful hints (too high/too low)
- 🎮 Multiple rounds gameplay

## How to Play

1. Run the game:
   ```bash
   python dice_guess_challenge.py
   ```

2. The game will roll a dice and you need to guess the number

3. Enter your guess (1-6) when prompted

4. You'll receive hints if your guess is too high or too low

5. Score points based on how many attempts it takes:
   - First attempt: 30 points
   - Second attempt: 20 points
   - Third attempt: 10 points

6. After each round, decide whether to play again or end the game

## Requirements

- Python 3.x
- No external libraries required (uses only built-in modules)

## Example Gameplay

```
==================================================
   Welcome to Dice Guess Challenge!
==================================================

Rules:
1. The computer will roll a dice (1-6)
2. Try to guess the number!
3. You have 3 attempts per round
4. Score points for correct guesses
5. Try to beat your high score!

==================================================
Round 1 | Current Score: 0 | High Score: 0
==================================================

--------------------------------------------------
New Round! The dice has been rolled...
You have 3 attempts to guess the number.
--------------------------------------------------

Attempt 1/3
Enter your guess (1-6): 4
Too high! Try again.

Attempt 2/3
Enter your guess (1-6): 2
Too low! Try again.

Attempt 3/3
Enter your guess (1-6): 3

🎉 Correct! You guessed it in 3 attempt(s)!
You earned 10 points!

🏆 New high score!

Round Score: 10
Total Score: 10

Play another round? (y/n):
```

## License

This project is part of the 100 Lines of Python Code repository.

## Contributing

Feel free to fork, improve, and submit pull requests!
