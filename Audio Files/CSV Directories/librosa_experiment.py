import os
import pandas as pd
import librosa
from librosa import feature as lf

# Paths to the audio files
control_path = '/Users/cameronalevy/Documents/research miso/audio clips/Clips/control/rainfall.wav'
misophonia_path = "/Users/cameronalevy/Documents/research miso/audio clips/Clips/gum chewing/gum_chewing.wav"

# List to store the extracted features
data = []

# Function to extract features from an audio file
def extract_features(file_path):
    print(f"extract_features started with {file_path}")
    #real extraction
    try:
        #Load the audio file
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return None
        print("file exists")

        y, sr = librosa.load(file_path, sr=None)
        print("audio loaded")

        #Extract features
        duration = librosa.get_duration(y=y, sr=sr)
        rms = lf.rms(y=y).mean()
        zcr = lf.zero_crossing_rate(y).mean()
        spectral_centroid = lf.spectral_centroid(y=y, sr=sr).mean()

        #Return features as a dictionary
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

# Extract features from each file
control_features = extract_features(control_path)
misophonia_features = extract_features(misophonia_path)

# Append features to the data list
if control_features:
    data.append(control_features)
if misophonia_features:
   data.append(misophonia_features)

# Create a DataFrame
df = pd.DataFrame(data)

# Check if DataFrame is empty
if df.empty:
    print("No features were extracted. Check the audio file paths or formats.")
else:
    # Save the DataFrame to a CSV file
    output_csv_path = '/Users/cameronalevy/Documents/research miso/audio_analysis.csv'
    df.to_csv(output_csv_path, index=False)
    print(f"Features extracted and saved to {output_csv_path}")
