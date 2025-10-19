# Typing Speed Racer 🏎️⌨️

A competitive typing speed game that tests your typing skills with real-time WPM (Words Per Minute) and accuracy tracking.

## Description

Typing Speed Racer is an interactive terminal-based game designed to help improve your typing speed and accuracy. The game presents random text prompts at different difficulty levels and measures your performance with instant feedback.

## Features

- **Multiple Difficulty Levels**: Choose from Easy, Medium, or Hard challenges
- **Real-time WPM Calculation**: Instantly see your typing speed in Words Per Minute
- **Accuracy Tracking**: Monitor your typing accuracy with percentage metrics
- **Colorful Terminal Interface**: Enhanced visual experience with ANSI color codes
- **Performance Feedback**: Get motivational feedback based on your results
- **Replayable**: Practice as many times as you want to improve your skills

## How to Play

1. Run the script:
   ```bash
   python typing_speed_racer.py
   ```
   or
   ```bash
   python3 typing_speed_racer.py
   ```

2. Select your difficulty level:
   - **Easy**: Short, simple sentences
   - **Medium**: Programming quotes and moderate length text
   - **Hard**: Long paragraphs with complex content

3. Read the text prompt carefully

4. Press ENTER when ready to start

5. Type the text as quickly and accurately as possible

6. Press ENTER when finished

7. View your results:
   - Time taken
   - Typing speed (WPM)
   - Accuracy percentage
   - Performance rating

## Performance Ratings

- **🏆 CHAMPION**: 60+ WPM with 95%+ accuracy
- **⭐ EXCELLENT**: 40+ WPM with 90%+ accuracy
- **👍 GOOD**: 20+ WPM with 70%+ accuracy
- **💪 Keep Practicing**: Below the above thresholds

## Requirements

- Python 3.6 or higher
- Terminal with ANSI color support (most modern terminals)

## Technical Details

### WPM Calculation

The game uses the standard formula for calculating Words Per Minute:
- 1 word = 5 characters (industry standard)
- WPM = (characters typed / 5) / (time in minutes)

### Accuracy Calculation

Accuracy is calculated as:
- Percentage of correctly typed characters compared to the original text
- Accuracy = (correct characters / total characters) × 100

## Controls

- **ENTER**: Start typing or submit your typed text
- **Ctrl+C**: Exit the game at any time
- **y/n**: Choose to play again after each round

## Code Structure

The game is organized into several key functions:

- `clear_screen()`: Clears the terminal display
- `print_banner()`: Displays the game title and branding
- `calculate_wpm()`: Computes typing speed
- `calculate_accuracy()`: Computes typing accuracy
- `get_difficulty()`: Handles difficulty selection
- `play_game()`: Main game logic
- `display_results()`: Shows performance metrics
- `main()`: Game loop and flow control

## Sample Output

```
╔══════════════════════════════════════════╗
║      TYPING SPEED RACER - v1.0          ║
║      Test Your Typing Skills!           ║
╚══════════════════════════════════════════╝

Select Difficulty Level:
  1. Easy (Short sentences)
  2. Medium (Programming quotes)
  3. Hard (Long paragraphs)

Enter your choice (1-3): 2

Type the following text:

"First solve the problem. Then write the code."

Press ENTER when ready to start...

GO! Start typing now!

>>> First solve the problem. Then write the code.

==================================================
RACE RESULTS
==================================================

  Difficulty: Medium
  Time Taken: 8.45 seconds
  Text Length: 47 characters
  Typing Speed: 66.63 WPM
  Accuracy: 100.0%

==================================================

🏆 CHAMPION! Outstanding performance!

Do you want to race again? (y/n):
```

## Tips for Improvement

1. **Focus on Accuracy First**: Speed will naturally improve with accuracy
2. **Use Proper Posture**: Sit upright with feet flat on the floor
3. **Position Your Hands**: Keep your fingers on the home row (ASDF JKL;)
4. **Don't Look at the Keyboard**: Train yourself to touch type
5. **Practice Regularly**: Consistency is key to improvement
6. **Start with Easy Level**: Build confidence before moving to harder levels

## Contributing

This project is part of the 100LinesOfPythonCode repository. Feel free to suggest improvements or report issues.

## Issue Reference

This implementation addresses issue [#1161](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1161) - Typing Speed Racer

## License

This project follows the license of the main 100LinesOfPythonCode repository.

## Author

Created as part of the Hacktoberfest contribution to 100LinesOfPythonCode.

---

**Happy Typing! 🚀**
