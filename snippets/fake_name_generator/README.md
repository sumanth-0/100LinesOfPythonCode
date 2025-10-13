# Fake Name Generator

## Description
A Python script that generates realistic fake names with associated country origins. The script uses predefined name patterns from various countries including USA, UK, India, Japan, Germany, France, Brazil, Spain, Italy, and China.

## Features
- Generate random human names with realistic first and last name combinations
- Support for 10 different countries with authentic name patterns
- Generate single or multiple names at once
- Optional country-specific name generation
- Clean command-line interface
- Under 100 lines of Python code

## Usage

### Basic Usage
Generate 10 random names from all countries:
```bash
python fake_name_generator.py
```

### Specify Number of Names
Generate a specific number of names:
```bash
python fake_name_generator.py 20
```

### Country-Specific Names
Generate names from a specific country:
```bash
python fake_name_generator.py 10 USA
python fake_name_generator.py 5 Japan
python fake_name_generator.py 15 India
```

## Supported Countries
- USA
- UK
- India
- Japan
- Germany
- France
- Brazil
- Spain
- Italy
- China

## Example Output
```
============================================================
Fake Name Generator
============================================================

Generating 10 fake name(s)...

 1. James Smith                    (Origin: USA)
 2. Oliver Taylor                  (Origin: UK)
 3. Aarav Kumar                    (Origin: India)
 4. Haruto Sato                    (Origin: Japan)
 5. Ben Müller                     (Origin: Germany)
 6. Louis Martin                   (Origin: France)
 7. Miguel Silva                   (Origin: Brazil)
 8. Hugo Garcia                    (Origin: Spain)
 9. Leonardo Rossi                 (Origin: Italy)
10. Wei Wang                       (Origin: China)

============================================================
Available countries: Brazil, China, France, Germany, India, Italy, Japan, Spain, UK, USA
Usage: python fake_name_generator.py [count] [country]
============================================================
```

## Requirements
- Python 3.x
- No external dependencies (uses only standard library)

## Contributing
This script is part of the 100 Lines of Python Code project. Contributions and improvements are welcome!

## License
This project follows the license of the main repository.
