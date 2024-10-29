Here’s an updated version of your README to reflect the changes for using Gradio and running `app.py`:

---

# Music Genre Classifier

This project classifies music genres using a Recurrent Neural Network (RNN) trained on audio features extracted from music files. It leverages the `librosa` library for audio processing, `tensorflow` for the model, and `pydub` for audio format conversion. The accuracy is 55% (for now).

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
pip install pandas librosa tensorflow pydub numpy gradio
```

## Usage

1. **Run the Gradio Interface**: You can start the Gradio interface to predict the genre of audio files.

   ```bash
   python Music_Genre_Classifier/app.py
   ```

2. **Upload an Audio File**: Open the Gradio interface in your web browser [http://127.0.0.1:7860](http://127.0.0.1:7860) (or the link  provided in the console after running the script). Upload your `.mp3` audio file through the interface.

3. **View Predictions**: The predicted genre will be displayed on the interface after processing the audio file.

## Dependencies

- `pandas`: For data manipulation and analysis.
- `librosa`: For audio and music analysis.
- `tensorflow`: For building and loading the neural network model.
- `pydub`: For audio file format conversion.
- `numpy`: For numerical operations.
- `gradio`: For creating a user-friendly interface for model predictions.

## How It Works

1. **Feature Extraction**: The audio file is loaded, and Mel-frequency cepstral coefficients (MFCC) are extracted to represent the audio features.

2. **Model Loading**: The pre-trained RNN model on the GTZAN dataset is loaded from the specified file path.

3. **Audio Conversion**: If your input file is in `.mp3` format, it is converted to `.wav` using `pydub`.

4. **Prediction**: The extracted features are fed into the model to predict the genre. The output is the genre label corresponding to the predicted index.

5. **Output**: The predicted genre is displayed in the Gradio interface.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to this project.

## License

This project is licensed under the MIT License.

---

Feel free to modify any sections further based on your specific project needs or additional features!