# Simple Markdown Converter

A lightweight Python utility to convert Markdown files to HTML or plain text format.

## Description

This tool converts Markdown-formatted text files into HTML or plain text, supporting common Markdown elements including headers, lists, bold/italic text, links, and code blocks.

## Features

- **Headers**: Supports H1 through H6 headers
- **Lists**: Converts unordered lists (*, -)
- **Text Formatting**: Bold (**text**) and italic (*text*)
- **Links**: Converts [text](url) format
- **Code**: Both inline `code` and code blocks (```)
- **Output Formats**: HTML or plain text

## Usage

### Basic Usage

```bash
# Convert to HTML (default)
python simple_markdown_converter.py input.md

# Convert to plain text
python simple_markdown_converter.py input.md -f text

# Save output to file
python simple_markdown_converter.py input.md -o output.html
python simple_markdown_converter.py input.md -f text -o output.txt
```

### Command Line Arguments

- `input_file`: Path to the input Markdown file (required)
- `-o, --output`: Output file path (optional, defaults to stdout)
- `-f, --format`: Output format - 'html' or 'text' (default: html)

## Example

**Input (example.md):**
```markdown
# My Document

This is a **bold** statement and this is *italic*.

## Features
- First item
- Second item

Visit [GitHub](https://github.com)
```

**Output (HTML):**
```html
<h1>My Document</h1>
<p>This is a <strong>bold</strong> statement and this is <em>italic</em>.</p>
<h2>Features</h2>
<ul>
<li>First item</li>
<li>Second item</li>
</ul>
<p>Visit <a href="https://github.com">GitHub</a></p>
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Author

Created as part of the 100 Lines of Python Code project.

## Issue Reference

Addresses Issue #789 - Simple Markdown Converter
