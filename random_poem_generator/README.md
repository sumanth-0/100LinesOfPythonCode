# Random Poem Generator

A Python CLI tool that generates random poems in various styles and lengths.

## Description

This program generates random poems using predefined word banks and templates to create poems in different styles including haiku, limerick, quatrain, free verse, sonnet, and acrostic. The generator combines adjectives, nouns, verbs, and prepositions creatively to produce unique poems each time.

## Features

- **Multiple Poem Styles**: Supports 6 different poem styles
  - Haiku (5-7-5 syllable pattern)
  - Limerick (AABBA rhyme scheme)
  - Quatrain (ABAB rhyme scheme)
  - Free verse (customizable line count)
  - Sonnet (14 lines)
  - Acrostic (based on a given word)

- **Customizable Output**: Control the number of poems generated and lines in free verse
- **Reproducible Results**: Use random seeds for consistent output
- **Rich Word Banks**: Includes extensive collections of adjectives, nouns, verbs, and rhyme patterns

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

```bash
# Clone or download this repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/random_poem_generator

# Make the script executable (optional)
chmod +x random_poem_generator.py
```

## Usage

### Basic Usage

```bash
# Generate a haiku (default)
python random_poem_generator.py

# Generate a limerick
python random_poem_generator.py --style limerick

# Generate a free verse poem with 8 lines
python random_poem_generator.py --style free --lines 8

# Generate an acrostic poem from a word
python random_poem_generator.py --style acrostic --word PYTHON

# Generate multiple poems
python random_poem_generator.py --style haiku --number 3

# Use a seed for reproducible results
python random_poem_generator.py --style sonnet --seed 42
```

### Command-Line Arguments

- `-s, --style {haiku,limerick,quatrain,free,sonnet,acrostic}`: Style of poem to generate (default: haiku)
- `-l, --lines INT`: Number of lines for free verse (default: 6)
- `-w, --word STRING`: Word for acrostic poem (required for acrostic style)
- `-n, --number INT`: Number of poems to generate (default: 1)
- `--seed INT`: Random seed for reproducibility

## Examples

### Haiku Example
```
silent moon whispers
through the ancient forest
time fades softly
```

### Limerick Example
```
There once was a gentle star
That danced in the night
With radiant grace so light
It would blooms out of sight
Until morning brought flight
```

### Free Verse Example
```
Golden dreams dance
Beneath the crimson sky, fleeting hope soars
Silver shadow trembles
Through the velvet night
Mystical heart remembers
Ancient soul whispers
```

## Code Structure

The program consists of:

1. **Word Banks**: Collections of adjectives, nouns, verbs, prepositions, and rhyme pairs
2. **PoemGenerator Class**: Contains methods for generating different poem styles
3. **CLI Interface**: Argument parsing and user interaction

## Contributing

Feel free to contribute by:
- Adding new word banks
- Implementing new poem styles
- Improving rhyme schemes
- Enhancing syllable counting

## License

This project is part of the 100LinesOfPythonCode repository. See the main repository for license information.

## Author

Contributed as part of Hacktoberfest 2025

## Related Issues

- Issue #1021: Random Poem Generator
