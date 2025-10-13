#!/usr/bin/env python3
import os
import sys
import re


def convert_to_markdown(text):
    """Convert plain text to markdown format."""
    lines = text.split('\n')
    markdown_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            markdown_lines.append('')
            continue
            
        # Convert headers (lines ending with :)
        if line.endswith(':'):
            markdown_lines.append(f"## {line[:-1]}")
        # Convert bullet points (lines starting with -, *, or •)
        elif line.startswith(('-', '*', '•')):
            content = line[1:].strip()
            markdown_lines.append(f"- {content}")
        # Convert numbered lists
        elif re.match(r'^\d+\.?\s+', line):
            content = re.sub(r'^\d+\.?\s+', '', line)
            markdown_lines.append(f"1. {content}")
        # Regular text
        else:
            markdown_lines.append(line)
    
    return '\n'.join(markdown_lines)


def process_file(input_file, output_file=None):
    """Process input file and convert to markdown."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        markdown_content = convert_to_markdown(content)
        
        if not output_file:
            output_file = os.path.splitext(input_file)[0] + '.md'
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"Converted: {input_file} -> {output_file}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File not found: {input_file}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def create_sample_file():
    """Create a sample text file for demonstration."""
    sample_content = """Introduction:
This is a sample document.

Features:
- Easy to use
- Fast conversion
- Supports headers
* Multiple bullet styles
• Unicode bullets too

Steps to follow:
1. Open the file
2. Run the converter
3. Check the output

Conclusion:
The conversion is complete."""
    
    with open('sample.txt', 'w', encoding='utf-8') as f:
        f.write(sample_content)
    print("Created sample.txt")


def main():
    """Main function."""
    print("Simple Markdown Converter")
    print("=" * 30)
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        input_file = input("Enter input file path (or press Enter for sample): ").strip()
        
        if not input_file:
            create_sample_file()
            input_file = 'sample.txt'
        
        output_file = input("Enter output file path (optional): ").strip() or None
    
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return
    
    if process_file(input_file, output_file):
        print("Conversion completed successfully!")


if __name__ == "__main__":
    main()