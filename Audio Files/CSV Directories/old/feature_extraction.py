import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths
valid_csv = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\valid_audioset_clips.csv"
output_visuals_dir = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\Visualizations"

# Create output directory for visualizations
os.makedirs(output_visuals_dir, exist_ok=True)

# Load the valid dataset
valid_clips = pd.read_csv(valid_csv)

# Function to extract features and create visualizations
def process_audio(row):
    clip_path = row['ClipPath']
    label = row['Labels']
    youtube_id = row['YouTubeID']

    try:
        # Load audio file
        y, sr = librosa.load(clip_path, sr=None)

        # Extract features (MFCCs, Spectrogram)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        spectrogram = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

        # Save waveform visualization
        plt.figure(figsize=(10, 4))
        librosa.display.waveshow(y, sr=sr)
        plt.title(f"Waveform - {youtube_id}")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.savefig(os.path.join(output_visuals_dir, f"{youtube_id}_waveform.png"))
        plt.close()

        # Save spectrogram visualization
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(spectrogram, sr=sr, x_axis='time', y_axis='log')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f"Spectrogram - {youtube_id}")
        plt.savefig(os.path.join(output_visuals_dir, f"{youtube_id}_spectrogram.png"))
        plt.close()

        # Return extracted features
        return {
            "YouTubeID": youtube_id,
            "Label": label,
            "MFCCs": mfccs.mean(axis=1).tolist(),  # Use mean MFCCs as features
        }

    except Exception as e:
        print(f"Error processing {clip_path}: {e}")
        return None

# Process all valid clips
processed_data = []
for _, row in valid_clips.iterrows():
    result = process_audio(row)
    if result:
        processed_data.append(result)

# Create a DataFrame from extracted features
features_df = pd.DataFrame(processed_data)
features_df.to_csv(r"C:\Users\matt0\PycharmProjects\miso\Audio Files\Processed\features.csv", index=False)
print("Feature extraction and visualization complete!")
