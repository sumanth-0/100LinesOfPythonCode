# Auto CSV Cleaner

A Python command-line tool to automatically clean CSV files by removing empty rows, duplicate rows, and handling missing values.

## Features

- **Remove Empty Rows**: Automatically detects and removes completely empty rows from CSV files
- **Remove Duplicates**: Identifies and eliminates duplicate rows while preserving unique data
- **Handle Missing Values**: Offers multiple strategies for dealing with missing or empty cells:
  - `remove`: Remove rows containing any missing values (default)
  - `fill`: Fill missing values with 'N/A'
  - `keep`: Keep rows as-is without modification

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

No installation required! Just download the `auto_csv_cleaner.py` file and run it.

## Usage

### Basic Usage

Clean a CSV file with default settings (removes empty rows, duplicates, and rows with missing values):

```bash
python auto_csv_cleaner.py input.csv
```

This will create a cleaned file named `input_cleaned.csv` in the same directory.

### Specify Output File

```bash
python auto_csv_cleaner.py input.csv output.csv
```

### Handle Missing Values

**Remove rows with missing values (default):**
```bash
python auto_csv_cleaner.py input.csv --strategy remove
```

**Fill missing values with 'N/A':**
```bash
python auto_csv_cleaner.py input.csv --strategy fill
```

**Keep rows with missing values:**
```bash
python auto_csv_cleaner.py input.csv --strategy keep
```

## Example

**Input CSV (messy.csv):**
```
Name,Age,City
John,25,NYC
Jane,30,LA
,,
John,25,NYC
Bob,,Chicago
```

**Command:**
```bash
python auto_csv_cleaner.py messy.csv --strategy fill
```

**Output CSV (messy_cleaned.csv):**
```
Name,Age,City
John,25,NYC
Jane,30,LA
Bob,N/A,Chicago
```

## Statistics

The tool provides helpful statistics during cleaning:
- Original number of rows
- Rows after removing empty entries
- Rows after removing duplicates
- Rows after handling missing values

## Contributing

This tool was created for issue [#1006](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1006) of the 100LinesOfPythonCode repository.

## License

Free to use and modify!

## Author

Contributed to 100LinesOfPythonCode - Hacktoberfest 2025
