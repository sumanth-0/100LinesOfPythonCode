# Typing Speed Racer 🏁

## Description

Typing Speed Racer is an interactive Python program that tests and improves your typing speed and accuracy. This competitive typing game calculates your Words Per Minute (WPM) and accuracy by comparing your typed text to sample texts. It's perfect for anyone looking to enhance their typing skills through gamified practice.

## Features

- **Multiple Sample Texts**: Practice with various texts of different difficulty levels
- **Real-time WPM Calculation**: Instantly see your typing speed in Words Per Minute
- **Accuracy Tracking**: Get precise accuracy percentage based on your performance
- **Performance Rating System**: Receive ratings from Novice to Expert based on your WPM and accuracy
- **Detailed Error Analysis**: See exactly where you made mistakes with the first 5 errors highlighted
- **Competitive Scoring**: Track your progress and aim for higher scores
- **Continuous Practice Mode**: Keep practicing with multiple rounds until you're ready to stop

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library modules)

## Installation

1. Clone or download this repository
2. Navigate to the `typing_speed_racer` folder
3. Run the program using Python:

```bash
python typing_speed_racer.py
```

## How to Use

1. **Start the Program**: Run `python typing_speed_racer.py` in your terminal
2. **Read the Sample Text**: A random sample text will be displayed
3. **Press ENTER**: When you're ready to start typing
4. **Type the Text**: Type the displayed text as quickly and accurately as possible
5. **View Results**: After pressing ENTER, see your comprehensive performance report including:
   - Time taken
   - Typing speed (WPM)
   - Accuracy percentage
   - Total errors
   - Error analysis
   - Performance rating
6. **Continue or Exit**: Choose to practice again or exit the program

## Performance Ratings

The game provides performance ratings based on your WPM and accuracy:

- **🏆 EXPERT**: 60+ WPM with 95%+ accuracy - Outstanding performance!
- **⭐ ADVANCED**: 45+ WPM with 90%+ accuracy - Excellent typing skills!
- **✓ INTERMEDIATE**: 30+ WPM with 85%+ accuracy - Good progress!
- **📚 BEGINNER**: 15+ WPM with 75%+ accuracy - Keep practicing!
- **🎯 NOVICE**: Below 15 WPM or below 75% accuracy - Practice makes perfect!

## Example Output

```
======================================================================
                    🏁 TYPING SPEED RACER - RESULTS 🏁
======================================================================

⏱️  Time Taken: 32.45 seconds
🚀 Typing Speed: 48.23 WPM
🎯 Accuracy: 92.5%
❌ Total Errors: 6

📋 Error Analysis:
   - Position 12: Expected 'h', got 'j'
   - Position 45: Expected 'e', got 'r'
   - Missing 2 characters

⭐ ADVANCED - Excellent typing skills!
======================================================================
```

## Technical Details

- **Lines of Code**: 218 lines (well-commented and documented)
- **Calculation Method**: Uses standard 5 characters = 1 word formula for WPM
- **Accuracy Algorithm**: Utilizes Python's `difflib.SequenceMatcher` for precise similarity comparison
- **Time Tracking**: High-precision time measurement using the `time` module

## Tips for Improvement

1. **Focus on Accuracy First**: High accuracy is more important than raw speed
2. **Practice Regularly**: Consistent practice leads to steady improvement
3. **Use Proper Finger Placement**: Follow touch typing guidelines for best results
4. **Don't Look at the Keyboard**: Train yourself to type without looking
5. **Take Breaks**: Avoid fatigue by taking regular breaks during practice sessions

## Author

Created as a solution for issue #1161 in the 100LinesOfPythonCode repository.

## License

This project is part of the 100LinesOfPythonCode collection and follows the repository's licensing terms.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the main repository's contributing guidelines.

---

**Happy Typing! 🚀**
