import pandas as pd
import librosa
import librosa.display
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
from pydub import AudioSegment
import gradio as gr

# Load the model
model = load_model(r'Music_Genre_Classifier\audio_classification_rnn.keras')

# Genre mapping
genres = {0:'Blues', 1:'Classical', 2:'Country', 3:'Disco', 
          4:'Hip-Hop', 5:'Metal', 6:'Pop', 7:'Reggae', 
          8:'Rock', 9:'Jazz'}

# Feature extraction
def features_extractor(file):
    audio, sample_rate = librosa.load(file, sr=None)
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    return mfccs_scaled_features

# Convert MP3 to WAV
def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")

# Prediction function
def predict_genre(mp3_file):
    # Convert mp3 to wav
    wav_file = "temp_converted_audio.wav"
    convert_mp3_to_wav(mp3_file.name, wav_file)
    
    # Extract features and make prediction
    features = features_extractor(wav_file)
    features = np.expand_dims(features, axis=0)
    features = np.expand_dims(features, axis=1)
    prediction = model.predict(features)
    predicted_index = np.argmax(prediction, axis=1)[0]
    
    return f"You're listening to {genres[predicted_index]}"

# Create Gradio interface
iface = gr.Interface(
    fn=predict_genre,
    inputs=gr.File(label="Upload an MP3 file"),
    outputs="text",
    title="Music Genre Classifier",
    description="Upload an MP3 file to predict its genre."
)

# Launch the interface
iface.launch()
