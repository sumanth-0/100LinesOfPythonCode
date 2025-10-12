# Random File Content Picker 🎲📄

A simple Python script that chooses a random line from a file and prints it each time it runs. Perfect for daily quotes, random tasks, motivational messages, or any line-based content!

## Features

- **Random Line Selection**: Picks a random line from any text file
- **Multiple Usage Modes**: Command line arguments or interactive input
- **Sample Content**: Auto-creates sample quotes file if none provided
- **Error Handling**: Graceful handling of missing files and permissions
- **File Statistics**: Shows total number of lines in the file
- **Clean Output**: Beautiful formatted display with emojis

## Usage

### Method 1: Interactive Mode
```bash
python random_file_picker.py
```
The script will prompt you for a file path, or create a sample quotes file if none provided.

### Method 2: Command Line Argument
```bash
python random_file_picker.py path/to/your/file.txt
```

### Method 3: Use Sample File
```bash
python random_file_picker.py
# Press Enter when prompted to use sample quotes
```

## Example Output

```
🎲 Random File Content Picker
========================================

📂 Reading from: sample_quotes.txt

==================================================
🎯 Random Pick:
   The only way to do great work is to love what you do. - Steve Jobs
==================================================

📊 File contains 10 lines
```

## File Format

The script works with any text file where each line contains content you want to randomly select from:

```
Quote 1
Quote 2
Quote 3
Task: Review project documentation
Task: Update website content
Remember to call mom
```

## Use Cases

- **Daily Quotes**: Motivational or inspirational quotes
- **Task Randomizer**: Random task selection from a to-do list
- **Decision Maker**: Random choices from a list of options
- **Learning Tool**: Random facts, vocabulary words, or study notes
- **Creative Prompts**: Writing prompts or creative challenges
- **Habit Tracker**: Random healthy habits or activities

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Error Handling

The script handles various scenarios gracefully:
- Missing files (offers to create sample file)
- Empty files
- Permission errors
- Invalid file paths
- Encoding issues

## Sample Content

If no file is provided, the script creates a sample file with 10 inspirational quotes from famous personalities.

## Customization

You can easily customize the script by:
- Modifying the sample quotes in the `create_sample_file()` function
- Changing the output format in the `main()` function
- Adding filters for specific line patterns
- Implementing weighted random selection

## Author

Created for issue #790 - 100 Lines of Python Code Project

## License

Open source - feel free to modify and enhance!