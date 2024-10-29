# Music Genre Classifier

This project classifies music genres using a Recurrent Neural Network (RNN) trained on audio features extracted from music files. It leverages the `librosa` library for audio processing, `tensorflow` for the model, and `pydub` for audio format conversion. The accuracy is 55%(for now).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Installation

Make sure you have Python installed on your machine. You can set up the required packages using pip. Create a virtual environment and install the dependencies as follows:

```bash
pip install pandas librosa tensorflow pydub numpy
```

## Usage

1. Place your `.mp3` audio file as `sample.mp3` in the `Music_Genre_Classifier` directory.
2. Run the script to predict the genre of the audio file:

```bash
python python Music_Genre_Classifier/musicgenre.py
```

## Dependencies

- `pandas`: For data manipulation and analysis.
- `librosa`: For audio and music analysis.
- `tensorflow`: For building and loading the neural network model.
- `pydub`: For audio file format conversion.
- `numpy`: For numerical operations.

## How It Works

1. **Feature Extraction**: The audio file is loaded, and Mel-frequency cepstral coefficients (MFCC) are extracted to represent the audio features.

2. **Model Loading**: The pre-trained RNN model on GTZAN dataset is loaded from the specified file path.

3. **Audio Conversion**: If your input file is in `.mp3` format, it is converted to `.wav` using `pydub`.

4. **Prediction**: The extracted features are fed into the model to predict the genre. The output is the genre label corresponding to the predicted index.

5. **Output**: The predicted genre is printed to the console.
 