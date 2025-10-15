# Email Subject Line Generator

## Description
A Python tool that generates catchy email subject lines for newsletters or promotions using random templates and adjectives. This generator helps marketers and content creators quickly create engaging subject lines that capture attention and improve email open rates.

## Features
- **Multiple Word Lists**: Includes curated lists of adjectives, action verbs, urgency words, and offers
- **10 Different Templates**: Various subject line patterns including emojis and urgency triggers
- **Customizable Output**: Generate any number of subject lines at once
- **CLI Interface**: Easy-to-use command-line interface with arguments
- **Marketing-Focused**: Designed specifically for promotional and newsletter campaigns

## Installation
No additional packages required - uses only Python standard library.

## Usage
```bash
# Generate 5 subject lines (default)
python email_subject_line_generator.py

# Generate custom number of subject lines
python email_subject_line_generator.py -n 10
python email_subject_line_generator.py --number 15
```

## Example Output
```
📧 Email Subject Line Generator

==================================================
1. Discover Exclusive Deal - Last Chance!
2. 🎁 Premium Offer Inside!
3. ⚡ Limited Time: Outstanding Bundle Available
4. Unlock 30% Off Amazing Products
5. Hey! Grab This Spectacular Sale
==================================================

Generated 5 subject lines!
```

## How It Works
The generator uses a template-based approach:
1. Randomly selects a subject line template
2. Fills template placeholders with random words from curated lists
3. Returns professionally formatted email subject lines
4. Includes emojis and urgency triggers to boost engagement

## Contributing
Feel free to submit issues or pull requests to improve the word lists or add new templates!

## Author
Created for the 100 Lines of Python Code repository

## Related Issue
Fixes #751 - Email Subject Line Generator
