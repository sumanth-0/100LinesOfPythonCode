# Reaction Timer Game ⚡

A Python-based reaction timer game that measures how fast you can respond after a random time delay. Test your reflexes and compete for the best reaction times!

## Description

This interactive console application challenges users to press Enter as quickly as possible after a visual prompt appears. The game includes multiple difficulty levels, tracks detailed statistics, and maintains a high score leaderboard.

## Features

- **Multiple Difficulty Levels**
  - Easy: 3 rounds with 2-5 second delays
  - Medium: 5 rounds with 1-4 second delays
  - Hard: 7 rounds with 0.5-3 second delays

- **Comprehensive Statistics**
  - Average reaction time
  - Best reaction time
  - Worst reaction time
  - Standard deviation (for consistency measurement)
  - Individual round-by-round results

- **High Score System**
  - Persistent storage of top 10 scores
  - JSON-based leaderboard
  - Track scores by difficulty level
  - Date and time stamps for each achievement

- **User-Friendly Interface**
  - Clear console display
  - Colorful emoji indicators 🔴⚡🌟👍✓⏰
  - Performance feedback after each round
  - Countdown timer before starting

- **Performance Ratings**
  - Amazing (< 200ms): Lightning fast!
  - Excellent (200-300ms): Very quick!
  - Good (300-400ms): Above average!
  - Not bad (400-500ms): Keep practicing!
  - Could be better (> 500ms): Try to focus!

## Requirements

- Python 3.6 or higher
- Standard library modules (no external dependencies)
  - `time`
  - `random`
  - `os`
  - `json`
  - `datetime`
  - `statistics`

## Installation

1. Clone the repository or download the `reaction_timer.py` file
2. Ensure you have Python 3.6+ installed
3. No additional packages need to be installed

## Usage

### Running the Game

```bash
python reaction_timer.py
```

### Main Menu Options

1. **Play Game**: Start a new reaction timer session
2. **View High Scores**: Display the leaderboard
3. **Exit**: Quit the application

### Game Flow

1. Enter your name (or remain anonymous)
2. Select difficulty level (1-3)
3. Get ready with a 3-2-1 countdown
4. Wait for the prompt after a random delay
5. Press Enter as quickly as possible when you see "🔴 PRESS ENTER NOW! 🔴"
6. View your reaction time and performance feedback
7. Complete all rounds for your chosen difficulty
8. Review detailed statistics
9. Your score is automatically saved to the leaderboard

## Game Mechanics

### Reaction Time Measurement

- The game measures time in milliseconds (ms)
- A random delay is introduced before each prompt
- The timer starts the moment the prompt appears
- The timer stops when you press Enter

### Scoring System

- Lower reaction times are better
- Average reaction time determines leaderboard ranking
- Scores are grouped by difficulty level
- Only the top 10 scores are retained

### High Score Storage

- Scores are saved in `high_scores.json` in the same directory
- The file is automatically created on first save
- Data includes: name, difficulty, average time, best time, and date

## Example Session

```
==================================================
           ⚡ REACTION TIMER GAME ⚡           
==================================================

Enter your name: Player1

Select Difficulty:
1. Easy (3 rounds, 2-5s delay)
2. Medium (5 rounds, 1-4s delay)
3. Hard (7 rounds, 0.5-3s delay)

Enter choice (1-3): 2

Get ready...
3...
2...
1...
GO!

Round 1/5
Wait for the prompt...

🔴 PRESS ENTER NOW! 🔴

Your reaction time: 287.45 ms
🌟 Excellent! Very quick!

--------------------------------------------------

Round 2/5
...
```

## Tips for Better Scores

1. **Stay Focused**: Minimize distractions and concentrate on the screen
2. **Be Ready**: Keep your finger near the Enter key
3. **Practice**: Your reaction time will improve with practice
4. **Choose Your Difficulty**: Start with Easy and work your way up
5. **Stay Consistent**: Try to maintain focus across all rounds

## Technical Details

### Class Structure

- **ReactionTimer**: Main game class containing all game logic
  - `__init__()`: Initialize game state
  - `clear_screen()`: Clear console display
  - `display_banner()`: Show game title
  - `get_player_info()`: Collect player name and difficulty
  - `countdown()`: Display countdown timer
  - `play_round()`: Execute a single game round
  - `rate_reaction()`: Provide performance feedback
  - `display_statistics()`: Show game results
  - `save_high_score()`: Persist score to file
  - `display_high_scores()`: Show leaderboard
  - `play_game()`: Main game loop

### Data Storage Format

High scores are stored in JSON format:

```json
[
  {
    "name": "Player1",
    "difficulty": "medium",
    "avg_reaction_time": 287.45,
    "best_time": 245.32,
    "date": "2025-10-19 12:30:45"
  }
]
```

## Troubleshooting

### Common Issues

1. **Permission Error when saving scores**
   - Ensure the script has write permissions in its directory
   - Try running from a location where you have full access

2. **Screen not clearing properly**
   - The clear screen function works differently on Windows vs Unix
   - This is normal and doesn't affect gameplay

3. **JSON decode error**
   - If `high_scores.json` becomes corrupted, delete it
   - The file will be recreated automatically

## Contributing

This project is part of the 100LinesOfPythonCode repository. Contributions are welcome!

## Related Issues

- Closes #1160: Reaction Timer implementation

## License

This project follows the license of the parent repository (100LinesOfPythonCode).

## Acknowledgments

- Created as part of the Hacktoberfest 2025 contribution
- Thanks to the 100LinesOfPythonCode community for the opportunity

## Future Enhancements

Potential improvements for future versions:

- Graphical user interface (GUI) using tkinter
- Sound effects for better feedback
- Online multiplayer mode
- Mobile app version
- Advanced statistics and charts
- Training mode with customizable parameters
- False start detection (pressing too early)

---

**Have fun testing your reflexes!** ⚡🎮
