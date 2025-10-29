# Typing Speed Test (terminal/curses)

Small terminal typing speed test implemented with Python and curses. It generates pseudo-real text (using NLTK words if available), runs an interactive typing session, and prints per-attempt and aggregate statistics (WPM, accuracy, chars/sec, corrections).

## Features
- Generates random text using NLTK word corpus (fallback list if not available).
- Interactive terminal UI using curses: shows target text, live colored input (green correct, red incorrect).
- Supports backspace counting as corrections.
- Multiple attempts with summary statistics (mean, stdev).

## Requirements

Install dependencies:
``` bash
python -m pip install nltk
```

On first run NLTK may download the 'words' corpus automatically.

## Usage
```
python typing_test.py [-r REPETITIONS] [-c CHARACTERS]
```
Defaults: REPETITIONS=1, CHARACTERS=100

Example:
```
python typing_test.py -r 3 -c 120
```

Controls during test:
- ENTER: start / finish attempt
- ESC: exit/cancel
- Backspace: delete last character (counts as a correction)

## Notes & tips
- Avoid running in terminals that don't support curses properly (some IDE integrated terminals may misbehave).
- The script measures WPM using only correct characters (5 chars = 1 word). Raw speed uses all typed characters.
- If you want reproducible text, replace `random.choice` with seeded RNG (e.g., random.seed(...)).

License: MIT (adapt as needed).
