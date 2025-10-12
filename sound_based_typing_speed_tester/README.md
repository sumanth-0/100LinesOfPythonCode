# Sound-Based Typing Speed Tester

A Python-based typing speed test application that provides audio feedback for each keypress, making the typing experience more engaging and interactive.

## Features

- **Random Text Prompts**: Get different practice texts each time you run the test
- **Sound Feedback**: Hear a beep sound with every keypress (requires pygame, falls back to system beep)
- **Performance Metrics**: 
  - Words Per Minute (WPM) calculation
  - Accuracy percentage
  - Time tracking
  - Character count
- **Cross-Platform**: Works on Windows, Linux, and macOS
- **Simple Interface**: Easy-to-use command-line interface

## Requirements

- Python 3.x
- pygame (optional, for better sound quality)

## Installation

1. Clone or download this repository
2. (Optional) Install pygame for enhanced sound:
   ```bash
   pip install pygame
   ```

## Usage

Run the script:
```bash
python sound_based_typing_speed_tester.py
```

### How to Use:
1. The program will display a random text sample
2. Press Enter when ready to start
3. Type the text as accurately and quickly as possible
4. A sound will play for each character you type
5. Press Enter when finished
6. View your results (WPM, accuracy, time)

## How It Works

1. **Sample Text Selection**: The program randomly selects from a pool of practice texts
2. **Sound Generation**: Uses pygame (if available) or system beep for keystroke feedback
3. **Timing**: Tracks elapsed time from start to finish
4. **WPM Calculation**: `(number of words) / (time in minutes)`
5. **Accuracy Calculation**: Percentage of correctly typed characters

## Example Output

```
============================================================
  SOUND-BASED TYPING SPEED TESTER
============================================================

Instructions:
- Type the text shown below as fast and accurately as you can
- A sound will play for each keypress
- Press Enter when done

Text to type:
The quick brown fox jumps over the lazy dog.

Press Enter when ready to start...

Start typing NOW!

============================================================
  RESULTS
============================================================
Time taken: 8.45 seconds
Words per minute (WPM): 56.33
Accuracy: 95.45%
Characters typed: 44
============================================================
```

## Notes

- If pygame is not installed, the program will use the system beep (\a) character
- On Windows, the program uses msvcrt for character-by-character input with immediate sound feedback
- On Unix-like systems (Linux/macOS), input is captured after pressing Enter

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is part of the 100 Lines of Python Code challenge.
