# Daily Affirmation Generator

A simple Python script that generates and displays random daily affirmations to boost positivity and motivation.

## Description

This script provides a collection of 25 positive affirmations that can be displayed randomly to help start your day with a positive mindset. It supports displaying single or multiple affirmations with command-line options.

## Features

- 25 curated positive affirmations
- Display single or multiple affirmations
- Clean, formatted console output
- Date-stamped affirmation headers
- Command-line interface
- No external dependencies (uses only Python standard library)

## Requirements

- Python 3.6 or higher

## Usage

### Basic Usage (Display one affirmation)

```bash
python daily_affirmation_generator.py
```

### Display Multiple Affirmations

```bash
python daily_affirmation_generator.py --count 5
```

### Help

```bash
python daily_affirmation_generator.py --help
```

## Example Output

```
============================================================
  Daily Affirmations for Sunday, October 12, 2025
============================================================

************************************************************
  I am worthy of love and respect.
************************************************************
```

## Command-Line Options

- `--count N` : Display N random affirmations (default: 1)
- `-h, --help` : Show help message and exit

## How It Works

The script uses Python's `random` module to select affirmations from a predefined list. Each affirmation is displayed with formatting to make it stand out. The script can display a single affirmation or multiple unique affirmations based on the user's preference.

## Contributing

Feel free to add more affirmations or suggest improvements!

## License

This project is part of the 100LinesOfPythonCode repository.
