# Personal Journal Entry Generator

A simple Python script that generates thoughtful daily journal prompts to help users reflect on their day and maintain a consistent journaling practice.

## Overview

This tool provides randomized writing prompts across five different categories:
- **Gratitude**: Prompts focused on appreciation and positive experiences
- **Reflection**: Questions that encourage self-awareness and growth
- **Goals**: Prompts related to personal objectives and progress
- **Creativity**: Fun and imaginative questions to spark creative thinking
- **Mindfulness**: Prompts centered on emotional awareness and self-care

## Features

- 📝 Generates random daily journal prompts
- 🎯 Organizes prompts by category for focused reflection
- 📅 Displays current date and time with each prompt
- 💾 Includes functionality to save journal entries to JSON format
- 🔄 Simple command-line interface
- ✨ Under 100 lines of Python code

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository or download the `journal_entry_generator.py` file
2. Navigate to the directory containing the script

## Usage

### Basic Usage

Run the script to get a random daily prompt:

```bash
python journal_entry_generator.py
```

This will display:
- Current date and time
- A randomly selected category
- A thoughtful writing prompt

### Example Output

```
============================================================
Journal Entry - 2025-10-12 at 08:30 PM
============================================================

Category: Gratitude

Today's Prompt:
What are three things you're grateful for today?

============================================================
```

## Code Structure

- `PROMPTS`: Dictionary containing categorized journal prompts
- `get_daily_prompt()`: Returns a random prompt (optionally from a specific category)
- `display_prompt_with_timestamp()`: Shows prompt with formatted date/time
- `save_entry()`: Saves journal entries to a JSON file (for future enhancement)

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository. Contributions and improvements are welcome!

## Related Issue

Created for issue #768: Personal Journal Entry Generator

## License

This code is part of the 100LinesOfPythonCode project. Please refer to the main repository for licensing information.

## Future Enhancements

- Add command-line arguments to select specific categories
- Implement interactive mode for writing and saving entries
- Add export options (Markdown, plain text)
- Include prompt history tracking to avoid repetition
- Add custom prompt management

---

*Happy journaling! 📓✨*
