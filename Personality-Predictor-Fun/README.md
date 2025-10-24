# Personality Predictor (for Fun)

Predicts a playful MBTI-like 4-letter type from 8 short A/B answers.

## Why it's interesting
- Under 100 lines, dependency-free, interactive or non-interactive
- Simple scoring across four dimensions with confidence levels
- Emoji flair and concise per-dimension explanation

## Files
- `predictor.py`: main script (<100 lines)
- `README.md`: this guide

## Usage
Interactive mode:

```bash
python predictor.py
```

Provide answers via CLI:

```bash
python predictor.py -a A,B,A,B,A,B,A,B
```

Sample output:

```bash
Type: ENTP 💡
E/I (Extraversion/Introversion): 2-0 conf=high; S/N (Sensing/Intuition): 0-2 conf=high; T/F (Thinking/Feeling): 2-0 conf=high; J/P (Judging/Perceiving): 0-2 conf=high
Disclaimer: This is playful and not a clinical assessment.
```

## Notes
- This is for entertainment and learning; not a psychological instrument.
- You can customize the questions/weights inside `predictor.py` while keeping the file under 100 lines.
