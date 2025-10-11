# Fun Fact Generator API Fetcher

## Description
A Python CLI tool that fetches and displays random fun facts from various public APIs. This script provides an easy way to get interesting facts, trivia, jokes, and advice from multiple sources with just a single command.

## Features
- 🎲 Multiple API sources to choose from
- 🌐 Fetches facts from 5 different APIs:
  - **uselessfacts**: Random interesting facts
  - **catfacts**: Fun facts about cats
  - **numbers**: Trivia about random numbers
  - **chucknorris**: Random Chuck Norris jokes
  - **advice**: Random advice slips
- 📋 List all available sources
- 💻 Simple command-line interface
- ⚡ Fast and lightweight (under 100 lines of code)

## Requirements
- Python 3.6+
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/fun_fact_generator_api_fetcher
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Basic Usage
Fetch a random fact from the default source (uselessfacts):
```bash
python fun_fact_generator_api_fetcher.py
```

### Choose a Specific Source
Fetch from a specific API source:
```bash
python fun_fact_generator_api_fetcher.py --source catfacts
python fun_fact_generator_api_fetcher.py -s numbers
python fun_fact_generator_api_fetcher.py -s chucknorris
python fun_fact_generator_api_fetcher.py -s advice
```

### List Available Sources
See all available fact sources:
```bash
python fun_fact_generator_api_fetcher.py --list
```

## Example Output

```
🎉 Fun Fact from uselessfacts:

The average person spends two weeks waiting for a traffic light to change.
```

## Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|----------|
| `--source` | `-s` | Choose fact source | `uselessfacts` |
| `--list` | `-l` | List all available sources | - |

## Available APIs

1. **Useless Facts API** - Random interesting facts
2. **Cat Facts API** - Fun facts about cats
3. **Numbers API** - Trivia about numbers
4. **Chuck Norris API** - Random Chuck Norris jokes
5. **Advice Slip API** - Random advice

## Error Handling
The script includes error handling for:
- Network connectivity issues
- API timeouts (5-second timeout)
- Invalid responses
- Failed API requests

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is part of the 100LinesOfPythonCode repository.

## Related Issue
This implementation solves issue #649 - Fun Fact Generator API Fetcher
