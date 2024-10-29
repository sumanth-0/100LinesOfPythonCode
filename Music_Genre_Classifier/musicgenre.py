import pandas as pd
import librosa 
import librosa.display
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model 


genres = {0:'Blues',1:'Classical',2:'Country',3:'Disco',4:'Hip-Hop',5:'Metal',6:'Pop',7:'Reggae',8:'Rock',9:'Jazz'}
#Feature extractor RNN
def features_extractor(file):
  audio,sample_rate = librosa.load(file,sr = None)
  mfccs_features = librosa.feature.mfcc(y=audio,sr=sample_rate,n_mfcc=40)
  mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
  return mfccs_scaled_features

model = load_model(r'Music_Genre_Classifier\audio_classification_rnn.keras')

#Conversion of mp3 to wav
from pydub import AudioSegment
def convert_mp3_to_wav(mp3_file,wav_file):
  audio = AudioSegment.from_mp3(mp3_file)
  audio.export(wav_file, format="wav")

file_path = r'Music_Genre_Classifier\sample.mp3'
wav_path = '/converted_audio.wav'

convert_mp3_to_wav(file_path,wav_path)
def predict_genre(file,model):
  features = features_extractor(file)

  features = np.expand_dims(features,axis  =  0)
  features = np.expand_dims(features,axis = 1)
  prediction = model.predict(features)
  predicted_index = np.argmax(prediction,axis = 1)[0]
  return predicted_index

predicted_genre_index = predict_genre(file_path,model)
print(f"You're listening to {genres[predicted_genre_index]}")