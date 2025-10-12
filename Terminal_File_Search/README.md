# Terminal File Search

A minimal Python script to search for files in directories by name patterns or extensions, displaying results with full paths.

## Features

- **Name Search**: Find files using wildcards (`*.py`, `test*`, `file.txt`)
- **Extension Search**: Search by file extension (`.py`, `.md`, `.txt`)
- **Recursive Search**: Searches through all subdirectories
- **Path Display**: Shows full paths for all matches
- **Interactive Mode**: Prompts for directory and pattern
- **Command Line**: Direct execution with arguments

## Usage

### Command Line
```bash
python file_search.py [directory] [pattern] [ext]
```

### Interactive Mode
```bash
python file_search.py
```

## Examples

### Search by Name Pattern
```bash
python file_search.py . "*.py"
python file_search.py /home/user "test*"
python file_search.py . "README.md"
```

### Search by Extension
```bash
python file_search.py . ".py"
python file_search.py /docs ".md"
python file_search.py . "txt" ext
```

### Interactive Example
```
Terminal File Search
=========================
Enter directory to search (or . for current): .
Enter search pattern (e.g., *.py, test*, file.txt): *.py

Searching in: /current/directory
Pattern: *.py (name)

Found 5 file(s) matching '*.py':
--------------------------------------------------
  1. ./script.py
  2. ./utils/helper.py
  3. ./tests/test_main.py
```

## Search Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| `*.py` | All Python files | `main.py`, `utils.py` |
| `test*` | Files starting with "test" | `test_main.py`, `testing.txt` |
| `README.md` | Exact filename | `README.md` |
| `.py` | Extension search | All `.py` files |
| `.md` | Extension search | All `.md` files |

## Requirements

- Python 3.6+
- No external dependencies

## Error Handling

- Permission denied directories are skipped
- Invalid directories show error message
- Empty results display appropriate message

## Author

Created for issue #788 - 100 Lines of Python Code Project