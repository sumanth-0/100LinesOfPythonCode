# Random Username Generator

A comprehensive Python tool for generating creative and unique usernames with various customization options.

## Features

- **Multiple Generation Styles**
  - Basic: Random alphanumeric usernames
  - Compound: Creative combinations using adjectives and nouns

- **Themed Generation**
  - Fantasy: Mystical and magical themes (Ethereal, Arcane, Celestial)
  - Sci-Fi: Futuristic and space themes (Quantum, Cyber, Nebula)
  - Nature: Natural world themes (Ocean, Mountain, Forest)
  - Tech: Technology-focused themes (Code, Pixel, Binary)

- **Customization Options**
  - Add numbers (prefix, suffix, or mixed)
  - Use separators (_, -, ., or none)
  - Leetspeak conversion
  - Adjustable length for basic style
  - Batch generation

## Usage

### Basic Usage

Generate a single username:
```bash
python random_username_generator.py
```

### Generate Multiple Usernames

Generate 10 usernames:
```bash
python random_username_generator.py -n 10
```

### Generate with Theme

Generate a fantasy-themed username:
```bash
python random_username_generator.py -t fantasy
```

Generate a sci-fi themed username with numbers:
```bash
python random_username_generator.py -t scifi --numbers
```

### Generate with Separators

Generate username with underscores:
```bash
python random_username_generator.py --separator _
```

### Generate Leetspeak Style

Generate username in leetspeak:
```bash
python random_username_generator.py --leetspeak
```

### Advanced Examples

Generate 5 tech-themed usernames with numbers and separators:
```bash
python random_username_generator.py -n 5 -t tech --numbers --separator _
```

Generate basic style username with custom length:
```bash
python random_username_generator.py -s basic -l 15
```

## Command Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|--------|
| `--count` | `-n` | Number of usernames to generate | 1 |
| `--style` | `-s` | Username style (basic/compound) | compound |
| `--theme` | `-t` | Theme (fantasy/scifi/nature/tech) | None |
| `--numbers` | | Add numbers to username | False |
| `--number-style` | | Number placement (prefix/suffix/mixed) | suffix |
| `--separator` | | Separator between parts (_/-/.) | none |
| `--leetspeak` | | Convert to leetspeak | False |
| `--length` | `-l` | Length for basic style | 10 |

## Example Output

```
🎲 Random Username Generator

==================================================
  1. MysticWarrior
  2. QuantumHunter
  3. ShadowNinja
  4. CrystalRanger
  5. CyberMage
==================================================

Generated 5 username(s)
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses standard library only)

## Implementation Details

The generator uses:
- **Word Lists**: Curated lists of adjectives, nouns, and themed words
- **Random Module**: For generating random combinations and numbers
- **String Module**: For alphanumeric character generation
- **Argparse**: For command-line interface

## Use Cases

- Creating usernames for new accounts
- Gaming handles
- Social media usernames
- Anonymous usernames
- Testing and development
- Username suggestions

## Contributing

This project is part of the 100LinesOfPythonCode repository. Contributions are welcome!

## License

This project follows the license of the parent repository.

## Related Issue

Resolves issue #676 - Random Username Generator
