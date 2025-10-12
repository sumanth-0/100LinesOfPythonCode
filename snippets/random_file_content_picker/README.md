# Random File Content Picker

## Description

A Python script that randomly selects and displays lines from a text file. Perfect for displaying random quotes, daily tasks, motivational messages, or any line-based content.

## Features

- 📝 Pick one or multiple random lines from any text file
- 🎲 Each run produces a different random selection
- 🔢 Optional line numbering for output
- 🛡️ Comprehensive error handling
- ⚡ Command-line interface for easy usage
- 📁 Works with any UTF-8 encoded text file

## Installation

No additional dependencies required! This script uses only Python standard library modules.

```bash
# Clone the repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/snippets/random_file_content_picker
```

## Usage

### Basic Usage

Pick a single random line from a file:

```bash
python random_file_content_picker.py quotes.txt
```

### Pick Multiple Lines

Select multiple random lines at once:

```bash
python random_file_content_picker.py quotes.txt --count 3
```

### Show Line Numbers

Display line numbers with the output:

```bash
python random_file_content_picker.py quotes.txt --numbered
```

### Combined Options

Combine multiple options:

```bash
python random_file_content_picker.py tasks.txt -c 5 -n
```

## Command-Line Arguments

- `filename` (required): Path to the text file to read from
- `-c, --count`: Number of random lines to pick (default: 1)
- `-n, --numbered`: Show line numbers with output
- `-h, --help`: Display help message

## Example

Create a sample quotes file:

```bash
echo "The only way to do great work is to love what you do. - Steve Jobs" >> quotes.txt
echo "Innovation distinguishes between a leader and a follower. - Steve Jobs" >> quotes.txt
echo "Stay hungry, stay foolish. - Steve Jobs" >> quotes.txt
echo "Life is what happens when you're busy making other plans. - John Lennon" >> quotes.txt
echo "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt" >> quotes.txt
```

Then run:

```bash
python random_file_content_picker.py quotes.txt --count 2 --numbered
```

Output:
```
============================================================
Random pick from: quotes.txt
============================================================

1. Innovation distinguishes between a leader and a follower. - Steve Jobs
2. Life is what happens when you're busy making other plans. - John Lennon

============================================================
```

## Use Cases

- 💡 **Daily Motivation**: Display random motivational quotes
- ✅ **Task Randomizer**: Randomly select tasks from a to-do list
- 📚 **Learning Tool**: Pick random vocabulary words or study topics
- 🎮 **Game Ideas**: Select random game prompts or challenges
- 🍽️ **Meal Planner**: Choose random recipes for the week
- 💭 **Writing Prompts**: Get random creative writing ideas

## Error Handling

The script handles various error scenarios:

- File not found
- Permission denied
- Empty files
- Invalid encoding
- Invalid count values

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Author

Created as part of the 100 Lines of Python Code project.

## Related Issue

This implementation addresses [Issue #790](https://github.com/sumanth-0/100LinesOfPythonCode/issues/790) - Random File Content Picker
