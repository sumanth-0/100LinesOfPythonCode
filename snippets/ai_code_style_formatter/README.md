# AI-Powered Code Style Formatter

## Description
An intelligent Python code formatter that automatically reformats Python code to conform to PEP8 and other style guidelines. This tool helps maintain consistent code quality across your Python projects.

## Features
- **Indentation Fixing**: Normalizes indentation to 4 spaces per level
- **Line Length Management**: Ensures lines don't exceed 79 characters (PEP8 standard)
- **Whitespace Formatting**: Adds proper spacing around operators and after commas
- **Blank Line Handling**: Adds appropriate blank lines between functions and classes
- **PEP8 Compliance**: Automatically applies PEP8 style guidelines

## Usage

```bash
python code_formatter.py <your_file.py>
```

### Example

```bash
python code_formatter.py messy_code.py
```

This will output the formatted version of your code to stdout.

## Requirements
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## How It Works

The formatter applies several formatting rules:

1. **Indentation**: Converts all indentation to 4-space standard
2. **Operators**: Adds spaces around mathematical and comparison operators
3. **Commas**: Ensures proper spacing after commas
4. **Blank Lines**: Adds 2 blank lines before top-level function/class definitions
5. **Trailing Whitespace**: Removes unnecessary trailing spaces

## Example Input/Output

**Before:**
```python
def hello(name,age):
  print("Hello "+name)
    print("Age: "+str(age))
```

**After:**
```python
def hello(name, age):
    print("Hello " + name)
    print("Age: " + str(age))
```

## Contributing
Contributions are welcome! Please ensure your code follows PEP8 guidelines and is under 100 lines.

## License
This project follows the repository's license.

## Issue Reference
Resolves issue #632: AI-Powered Code Style Formatter
