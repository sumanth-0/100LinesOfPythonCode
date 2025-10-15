# Song Mood Predictor

## Description
A Python script that predicts the mood of a song (happy, sad, energetic, or neutral) based on lyrics sentiment analysis. The script analyzes the lyrics by identifying mood-specific keywords and calculating mood scores.

## Features
- **Mood Detection**: Identifies whether a song is happy, sad, energetic, or neutral
- **Keyword-based Analysis**: Uses predefined mood keywords for sentiment analysis
- **Interactive Mode**: Allows users to input lyrics interactively
- **Command-line Support**: Accepts lyrics as command-line arguments
- **Detailed Scoring**: Provides mood scores for all categories

## Requirements
- Python 3.x
- No external dependencies required (uses only standard library)

## Installation
1. Clone the repository
2. Navigate to the `song_mood_predictor` folder
3. Run the script using Python 3

## Usage

### Interactive Mode
Run the script without arguments and enter lyrics when prompted:
```bash
python song_mood_predictor.py
```

Then enter your lyrics line by line. Press Enter twice to finish input.

### Command-line Mode
Provide lyrics as command-line arguments:
```bash
python song_mood_predictor.py "I'm so happy dancing in the sunshine with joy and love"
```

## Example Output
```
==================================================
SONG MOOD PREDICTOR
==================================================

Lyrics (first 100 chars): I'm so happy dancing in the sunshine with joy and love...

Predicted Mood: HAPPY

Mood Scores:
  Happy: 4
  Sad: 0
  Energetic: 1
==================================================
```

## How It Works
1. **Preprocessing**: Converts lyrics to lowercase and removes punctuation
2. **Tokenization**: Splits lyrics into individual words
3. **Mood Scoring**: Counts occurrences of mood-specific keywords
4. **Prediction**: Selects the mood with the highest score
5. **Output**: Displays the predicted mood and detailed scores

## Mood Keywords
- **Happy**: joy, happy, love, smile, laugh, dancing, celebration, sunshine, etc.
- **Sad**: sad, cry, tears, lonely, heartbreak, pain, sorrow, lost, etc.
- **Energetic**: run, jump, power, strong, energy, fire, wild, alive, etc.

## Contributing
Feel free to fork this repository and submit pull requests for improvements!

## License
This project is open source and available under the MIT License.
