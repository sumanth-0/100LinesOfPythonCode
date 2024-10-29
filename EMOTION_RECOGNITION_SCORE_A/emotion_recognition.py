
# Import libraries
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import sounddevice as sd

# Load pre-trained emotion recognition model
model = load_model("emotion_recognition_model.h5")
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('emotion_classes.npy')  # Load encoded emotion classes

def extract_features(audio_data, sample_rate=22050):
    # Extract audio features from the recorded audio
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def predict_emotion(audio_data, sample_rate=22050):
    features = extract_features(audio_data, sample_rate)
    features = np.expand_dims(features, axis=0)
    prediction = model.predict(features)
    predicted_emotion = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_emotion[0]

# Record and analyze audio
def record_and_analyze_emotion(duration=3, sample_rate=22050):
    print("Recording for {} seconds...".format(duration))
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until recording is finished
    audio_data = audio_data.flatten()  # Flatten to 1D array
    emotion = predict_emotion(audio_data, sample_rate)
    print("Detected Emotion:", emotion)

# Run the emotion recognition
record_and_analyze_emotion()
