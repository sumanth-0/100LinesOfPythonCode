# Blackjack Simplified

A console-based implementation of the classic Blackjack card game in Python.

## Description

This is a simplified version of Blackjack (also known as 21) that you can play directly in your terminal. The game features a dealer with AI logic, proper card shuffling, and automatic Ace value adjustment.

## Features

- 🎴 Standard 52-card deck with proper shuffling
- 🤖 Dealer AI that follows standard casino rules (stands on 17)
- ♠️ Card suits displayed with Unicode symbols
- 🎯 Automatic Ace value adjustment (11 or 1)
- 🔄 Play multiple rounds
- 💯 Under 100 lines of clean Python code

## How to Play

1. Run the game:
   ```bash
   python blackjack_simplified.py
   ```

2. You and the dealer are each dealt two cards
3. The dealer's first card is hidden
4. Choose to **Hit** (h) to take another card or **Stand** (s) to keep your current hand
5. Try to get as close to 21 as possible without going over
6. If you go over 21, you bust and lose
7. The dealer must hit until reaching at least 17
8. Whoever is closest to 21 without busting wins!

## Game Rules

- Number cards (2-10) are worth their face value
- Face cards (J, Q, K) are worth 10 points
- Aces are worth 11 points, or 1 point if 11 would cause a bust
- Blackjack (21 with first two cards) is an instant win
- Dealer must hit on 16 or less and stand on 17 or more

## Requirements

- Python 3.x
- No external dependencies required

## Example Output

```
=== Blackjack Simplified ===
Dealer's hand: [Hidden] 7♠
Player's hand: K♥ 5♦ (Value: 15)
Hit (h) or Stand (s)? h
Player's hand: K♥ 5♦ 4♣ (Value: 19)
Hit (h) or Stand (s)? s

Dealer's turn...
Dealer's hand: 10♠ 7♠ (Value: 17)
You win! 19 vs 17
```

## Contributing

This project was created as part of the 100 Lines of Python Code challenge. See the main repository for contribution guidelines.

## License

See the main repository for license information.

## Issue Reference

Addresses issue #1170 - Blackjack Simplified
