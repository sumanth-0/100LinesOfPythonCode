# Personalized Tarot Card Pull

## Description
A Python script that provides personalized tarot card readings based on user information and input. This tool draws tarot cards from the Major Arcana and provides interpretations customized for the user's question and personal details.

## Features
- **Personalized readings**: Uses user's name, birthdate, and question to generate unique, consistent readings
- **Multiple spread options**:
  - Single card draw for quick insights
  - Three-card spread (Past, Present, Future)
  - Five-card spread for detailed readings
- **Complete Major Arcana**: All 22 Major Arcana cards with meanings
- **Consistent results**: Same inputs on the same day produce same cards (uses deterministic seeding)
- **Beautiful formatting**: Well-formatted output with clear card positions and meanings

## Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation
1. Clone this repository or download the script
2. No additional installation needed - uses only Python standard library

## Usage
Run the script from the command line:
```bash
python tarot_card_pull.py
```

Follow the prompts:
1. Enter your name
2. Enter your birthdate (format: YYYY-MM-DD)
3. Enter a question you seek guidance on
4. Choose the number of cards (1, 3, or 5)

### Example
```
Welcome to Personalized Tarot Card Pull!

Enter your name: Alice
Enter your birthdate (YYYY-MM-DD): 1990-05-15
What question do you seek guidance on? What should I focus on this week?

How many cards would you like to draw?
1 - Single card (Quick insight)
3 - Three-card spread (Past, Present, Future)
5 - Five-card spread (Detailed reading)

Enter number (1, 3, or 5): 3

============================================================
   Personalized Tarot Reading for Alice
============================================================

Question: What should I focus on this week?

Past: The Magician
Meaning: Manifestation, resourcefulness, power
------------------------------------------------------------

Present: The Star
Meaning: Hope, faith, purpose, renewal
------------------------------------------------------------

Future: The Sun
Meaning: Positivity, fun, warmth, success
------------------------------------------------------------

============================================================
Thank you for using Personalized Tarot Card Pull!
============================================================
```

## How It Works
1. **Personalization**: Combines user's name, birthdate, and question with the current date to create a unique seed
2. **Deterministic randomness**: Uses the seed to ensure consistent results for the same inputs on the same day
3. **Card selection**: Randomly selects the requested number of cards from the Major Arcana
4. **Interpretation**: Displays each card with its position and meaning

## Tarot Cards Included
All 22 Major Arcana cards:
- The Fool, The Magician, The High Priestess, The Empress, The Emperor
- The Hierophant, The Lovers, The Chariot, Strength, The Hermit
- Wheel of Fortune, Justice, The Hanged Man, Death, Temperance
- The Devil, The Tower, The Star, The Moon, The Sun
- Judgement, The World

## Customization
You can easily customize the script by:
- Adding Minor Arcana cards to the `MAJOR_ARCANA` dictionary
- Modifying card meanings
- Adding new spread patterns
- Changing the formatting style

## Note
This tool is for entertainment and reflection purposes. Tarot readings should not replace professional advice for important life decisions.

## Line Count
This script contains 97 lines of Python code, well under the 100-line limit!

## License
Feel free to use, modify, and distribute this code.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## Author
Created for the 100LinesOfPythonCode project - Issue #622
