# Product Review Emotion Detector

Detects three emotions — anger, joy, trust — from review text in under 100 lines of Python.

## Why it's interesting
- Lexicon-based scoring with tiny heuristic stemming (no heavy dependencies)
- Negation window flips/attenuates sentiment for the next few tokens
- Emphasis boosts via ALL CAPS, exclamation marks, and elongated words

## File structure
- `detector.py`: the detector script (<100 lines)
- `README.md`: this guide

## Usage
Analyze a single text:

```bash
python detector.py "I loved the product but shipping was terrible!"
```

Analyze multiple reviews (one per line):

```bash
python detector.py -f reviews.txt
```

Sample output:

```bash
joy	anger=0.00	joy=1.50	trust=0.25	| I LOVED this, AMAZING and sturdy!!
not_joy	anger=0.00	joy=-0.70	trust=0.00	| not amazing
anger	anger=1.20	joy=0.00	trust=0.00	| terrible, awful packaging!!!
trust	anger=0.00	joy=0.20	trust=1.10	| solid and dependable build
neutral	anger=0.00	joy=0.00	trust=0.00	| it arrived on Tuesday
```

## Notes
- The lexicon is intentionally small for clarity; expand words while keeping the file <100 lines.
- Heuristics are simple and fast; for production accuracy, consider larger lexicons or ML models.
