import os
import glob
import pandas as pd
import librosa
from librosa import feature as lf

#path to audio files
audio_directory = '/Users/cameronalevy/Documents/research miso/audio clips/Clips'

#list to store the extracted features
data = []

#extract features from audio file
def extract_features(file_path):
    print(f"extract_features started with {file_path}")

    try:
        y, sr = librosa.load(file_path, sr=None)
        print("audio loaded")

        #extract features
        duration = librosa.get_duration(y=y, sr=sr)
        rms = lf.rms(y=y).mean()
        zcr = lf.zero_crossing_rate(y).mean()
        spectral_centroid = lf.spectral_centroid(y=y, sr=sr).mean()

        #return features as dictionary
        return {
            'file_path': file_path,
            'duration': duration,
            'rms': rms,
            'zcr': zcr,
            'spectral_centroid': spectral_centroid
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

#iterates over all audio files in the directory
for file_path in glob.glob(os.path.join(audio_directory, '**', '*.wav'), recursive=True):
    features = extract_features(file_path)
    if features:
        data.append(features)

#create dataframe
df = pd.DataFrame(data)

#check if dataframe is empty
if df.empty:
    print("No features were extracted. Check the audio file paths or formats.")
else:
    #save the dataframe to a CSV file
    output_csv_path = '/Users/cameronalevy/Documents/research miso/audio_analysis.csv'
    df.to_csv(output_csv_path, index=False)
    print(f"Features extracted and saved to {output_csv_path}")
