# Emoji Memory Match Game 🎮

A fun and interactive memory card matching game featuring emojis! Test your memory by matching pairs of emoji cards.

## 🎯 Features

- **Multiple Grid Sizes**: Choose from 2x2, 4x4, or 6x6 grids
- **Rich Emoji Collection**: 48+ different emojis across various categories
- **Score Tracking**: Track your attempts and matches
- **Time Tracking**: See how fast you can complete the game
- **Efficiency Calculation**: Get your performance rating
- **User-Friendly Interface**: Clear console-based UI with intuitive controls

## 🚀 How to Play

1. Run the game:
   ```bash
   python emoji_memory_match.py
   ```

2. Select your preferred grid size (2, 4, or 6)

3. The game board will display with hidden cards marked as `?`

4. Enter coordinates (row and column) to flip cards:
   - First card: Enter `row col` (e.g., `0 1`)
   - Second card: Enter `row col` (e.g., `2 3`)

5. Match all emoji pairs to win!

6. Type `quit` anytime to exit the game

## 📋 Game Rules

- Select two cards per turn by entering their row and column coordinates
- If the cards match, they stay revealed with a checkmark (✓)
- If they don't match, they flip back over
- Remember card positions to make matches faster
- The game ends when all pairs are matched

## 🎨 Emoji Categories

The game includes emojis from various categories:
- 🎮 Entertainment (games, music, art)
- ⚽ Sports (balls, activities)
- 🍎 Food (fruits)
- 🐶 Animals (various cute creatures)
- 🌸 Nature (flowers, elements)
- ⭐ Symbols (stars, sparkles)

## 📊 Game Statistics

After completing the game, you'll see:
- **Total Attempts**: Number of tries it took to match all pairs
- **Time Taken**: How long you took to complete the game
- **Efficiency**: Your performance percentage (perfect score = 100%)

## 💡 Tips

- Start with smaller grid sizes (2x2) to learn the game
- Focus on remembering card positions after each flip
- Try to create a mental map of the board
- Challenge yourself with larger grids for more difficulty

## 🛠️ Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## 🎮 Example Gameplay

```
==================================================
   🎮 EMOJI MEMORY MATCH GAME 🎮
==================================================

Attempts: 5 | Matches: 3/8

     0    1    2    3  

 0   ✓    ?    ?    ✓  
 1   ?    🎮   ?    ?  
 2   ✓    ?    ✓    ?  
 3   ?    ?    ?    🎮  
```

## 🎯 Challenge Yourself

- **Beginner**: 2x2 grid (2 pairs)
- **Intermediate**: 4x4 grid (8 pairs)
- **Expert**: 6x6 grid (18 pairs)

## 📝 Controls Summary

- Enter position as: `row col` (space-separated)
- Coordinates start from 0
- Type `quit` to exit anytime
- Press Enter to continue after matches

## 🏆 Goal

Match all emoji pairs in the fewest attempts and shortest time possible!

---

**Have fun playing! 🎉**

Created for issue #1159 in the 100LinesOfPythonCode repository.
