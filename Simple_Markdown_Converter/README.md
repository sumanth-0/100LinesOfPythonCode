# Simple Markdown Converter

A minimal Python script that converts plain text files to markdown format with automatic header and bullet list detection.

## Features

- **Header Detection**: Lines ending with `:` become `## Headers`
- **Bullet Lists**: Lines starting with `-`, `*`, or `•` become markdown bullets
- **Numbered Lists**: Lines starting with numbers become ordered lists
- **Auto Output**: Automatically names output file with `.md` extension
- **Sample Generation**: Creates sample file for testing

## Usage

### Command Line
```bash
python markdown_converter.py input.txt [output.md]
```

### Interactive Mode
```bash
python markdown_converter.py
```

## Conversion Rules

| Input | Output |
|-------|--------|
| `Header:` | `## Header` |
| `- Item` | `- Item` |
| `* Item` | `- Item` |
| `• Item` | `- Item` |
| `1. Item` | `1. Item` |
| `Regular text` | `Regular text` |

## Example

**Input (sample.txt):**
```
Introduction:
This is a sample document.

Features:
- Easy to use
- Fast conversion
* Multiple bullet styles

Steps:
1. Open file
2. Run converter
```

**Output (sample.md):**
```markdown
## Introduction
This is a sample document.

## Features
- Easy to use
- Fast conversion
- Multiple bullet styles

## Steps
1. Open file
1. Run converter
```

## Requirements

- Python 3.6+
- No external dependencies

## Author

Created for issue #789 - 100 Lines of Python Code Project