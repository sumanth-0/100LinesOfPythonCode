#!/usr/bin/env python3
"""
Simple Markdown Converter
Converts Markdown to HTML and plain text formats.
Supports headers, lists, bold, italic, links, and code blocks.
"""

import re
import sys
import argparse


class MarkdownConverter:
    """A simple Markdown to HTML/plaintext converter."""
    
    def __init__(self):
        self.html_output = []
        self.text_output = []
    
    def convert_to_html(self, markdown_text):
        """Convert markdown text to HTML."""
        lines = markdown_text.split('\n')
        in_code_block = False
        in_list = False
        
        for line in lines:
            # Handle code blocks
            if line.strip().startswith('```'):
                if in_code_block:
                    self.html_output.append('</code></pre>')
                    in_code_block = False
                else:
                    self.html_output.append('<pre><code>')
                    in_code_block = True
                continue
            
            if in_code_block:
                self.html_output.append(line)
                continue
            
            # Handle headers
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if header_match:
                level = len(header_match.group(1))
                content = header_match.group(2)
                content = self._process_inline(content)
                self.html_output.append(f'<h{level}>{content}</h{level}>')
                continue
            
            # Handle unordered lists
            if re.match(r'^[*-]\s+', line):
                if not in_list:
                    self.html_output.append('<ul>')
                    in_list = True
                content = re.sub(r'^[*-]\s+', '', line)
                content = self._process_inline(content)
                self.html_output.append(f'<li>{content}</li>')
                continue
            else:
                if in_list:
                    self.html_output.append('</ul>')
                    in_list = False
            
            # Handle empty lines
            if not line.strip():
                self.html_output.append('<br>')
                continue
            
            # Handle regular paragraphs
            processed_line = self._process_inline(line)
            self.html_output.append(f'<p>{processed_line}</p>')
        
        # Close any open list
        if in_list:
            self.html_output.append('</ul>')
        
        return '\n'.join(self.html_output)
    
    def _process_inline(self, text):
        """Process inline markdown elements like bold, italic, links."""
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Links
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
        # Inline code
        text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
        return text
    
    def convert_to_plaintext(self, markdown_text):
        """Convert markdown text to plain text (strip formatting)."""
        lines = markdown_text.split('\n')
        
        for line in lines:
            # Remove markdown syntax
            line = re.sub(r'^#{1,6}\s+', '', line)  # Headers
            line = re.sub(r'^[*-]\s+', '• ', line)  # Lists
            line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)  # Bold
            line = re.sub(r'\*(.+?)\*', r'\1', line)  # Italic
            line = re.sub(r'\[(.+?)\]\((.+?)\)', r'\1', line)  # Links
            line = re.sub(r'`(.+?)`', r'\1', line)  # Code
            self.text_output.append(line)
        
        return '\n'.join(self.text_output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML or plain text')
    parser.add_argument('input_file', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument('-f', '--format', choices=['html', 'text'], default='html',
                        help='Output format (default: html)')
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f'Error: File {args.input_file} not found')
        sys.exit(1)
    
    converter = MarkdownConverter()
    
    if args.format == 'html':
        result = converter.convert_to_html(markdown_content)
    else:
        result = converter.convert_to_plaintext(markdown_content)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'Output written to {args.output}')
    else:
        print(result)
