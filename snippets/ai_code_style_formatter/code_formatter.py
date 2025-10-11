#!/usr/bin/env python3
"""
AI-Powered Code Style Formatter
Automatically reformats Python code to conform to PEP8 and other style guidelines.
"""
import re
import sys

class CodeStyleFormatter:
    """Formats Python code according to PEP8 standards."""
    
    def __init__(self, code: str):
        self.code = code
        self.lines = code.split('\n')
    
    def format_indentation(self) -> str:
        """Fix indentation to 4 spaces per level."""
        formatted_lines = []
        for line in self.lines:
            stripped = line.lstrip()
            if not stripped:
                formatted_lines.append('')
                continue
            # Count leading spaces/tabs and normalize to 4-space indentation
            indent = len(line) - len(stripped)
            level = indent // 4
            formatted_lines.append('    ' * level + stripped)
        return '\n'.join(formatted_lines)
    
    def fix_line_length(self, max_length: int = 79) -> str:
        """Ensure lines don't exceed max_length."""
        formatted_lines = []
        for line in self.lines:
            if len(line) <= max_length:
                formatted_lines.append(line)
            else:
                # Simple break at comma or space
                indent = len(line) - len(line.lstrip())
                words = line.split()
                current_line, current_length = [], indent
                for word in words:
                    if current_length + len(word) + 1 <= max_length:
                        current_line.append(word)
                        current_length += len(word) + 1
                    else:
                        formatted_lines.append(' '.join(current_line))
                        current_line = [' ' * indent + word]
                        current_length = indent + len(word)
                if current_line:
                    formatted_lines.append(' '.join(current_line))
        return '\n'.join(formatted_lines)
    
    def fix_whitespace(self) -> str:
        """Fix whitespace around operators and commas."""
        formatted = self.code
        # Add space around operators
        formatted = re.sub(r'(\w)([+\-*/%=<>!])([\w(])', r'\1 \2 \3', formatted)
        # Fix space after comma
        formatted = re.sub(r',(\S)', r', \1', formatted)
        # Remove trailing whitespace
        formatted = '\n'.join(line.rstrip() for line in formatted.split('\n'))
        return formatted
    
    def fix_blank_lines(self) -> str:
        """Add proper blank lines between functions and classes."""
        lines = self.code.split('\n')
        formatted = []
        prev_line = ''
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Add 2 blank lines before class/function definitions
            if (stripped.startswith('def ') or stripped.startswith('class ')) and prev_line and not prev_line.isspace():
                if i > 0 and lines[i-1].strip():
                    formatted.append('')
                    formatted.append('')
            formatted.append(line)
            prev_line = line
        return '\n'.join(formatted)
    
    def format(self) -> str:
        """Apply all formatting rules."""
        self.code = self.fix_whitespace()
        self.lines = self.code.split('\n')
        self.code = self.format_indentation()
        self.code = self.fix_blank_lines()
        return self.code.strip() + '\n'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
    else:
        print("Usage: python code_formatter.py <file.py>")
        sys.exit(1)
    formatter = CodeStyleFormatter(code)
    print(formatter.format())
