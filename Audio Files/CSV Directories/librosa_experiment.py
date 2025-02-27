import os
import glob
import pandas as pd
import librosa
import librosa.display
from librosa import feature as lf
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import butter, sosfiltfilt

#define a bandpass filter for 2500-5500 Hz
def bandpass_filter(signal, sr, lowcut=2500, highcut=5500, order=5):
    nyquist = 0.5 * sr
    low = lowcut / nyquist
    high = highcut / nyquist
    sos = butter(order, [low, high], btype='band', output='sos')
    return sosfiltfilt(sos, signal, axis=0)

#path to all audio files
audio_directory = '/Users/cameronalevy/Documents/research miso/audio clips/Clips'
audio_directory1 = '/Users/cameronalevy/Documents/research miso/audio clips/withNoise'

#list to store the extracted features
data = []

def categorize_file(file_name):
    """assigns a category from file name"""
    category_mapping = {
        "apple": "apple crunch",
        "gum": "chewing gum",
        "chips": "crunching chips",
        "breathing": "breathing",
        "typing": "typing",
        "rainfall": "rainfall",
        "printer": "printer",
        "sniff": "sniffling",
        "music": "music",
        "smack": "lips smacking"
    }
    file_name = file_name.lower()

    #check for keyword
    for keyword, category in category_mapping.items():
        if keyword in file_name:
            return category  #returns a category

    return "unknown"  #default category if no match found

#extract features from audio file
def extract_features(audio_file_path):
    print(f"extract_features started with {audio_file_path}")

    try:
        y, sr = librosa.load(audio_file_path, sr=None)
        print("audio loaded")

        #extract features
        rms = lf.rms(y=y).mean()
        zcr = lf.zero_crossing_rate(y=y).mean()
        chroma = lf.chroma_stft(y=y, sr=sr).mean()
        tonnetz = lf.tonnetz(y=librosa.effects.harmonic(y), sr=sr).mean()
        filtered_signal = bandpass_filter(y, sr)
        energy_2500_5500hz = np.sum(filtered_signal ** 2) / len(filtered_signal)
        from scipy.signal import hilbert
        analytic_signal = hilbert(y)
        amplitude_envelope = np.abs(analytic_signal)
        modulation_spectrum = fft(amplitude_envelope)
        frequencies =fftfreq(len(amplitude_envelope), d=1/sr)
        modulation_mask = (frequencies >= 1) & (frequencies <= 16)
        modulation_energy = np.sum(np.abs(modulation_spectrum[modulation_mask]) ** 2)

        category = categorize_file(os.path.basename(audio_file_path))

        #return features as dictionary
        return {
            'file_path': file_path,
            'rms': rms,
            'zcr': zcr,
            'chroma': chroma,
            'tonnetz': tonnetz,
            'category': category,
            "energy_2500_5500Hz": energy_2500_5500hz,
            "modulation_energy_1_16Hz": modulation_energy
        }
    except Exception as e:
        print(f"Error processing {audio_file_path}: {e}")
        return None

#iterates over all audio files in both directories to get the features
for file_path in glob.glob(os.path.join(audio_directory, '**', '*.wav'), recursive=True):
    features = extract_features(file_path)
    if features:
        data.append(features)

for file_path in glob.glob(os.path.join(audio_directory1, '**', '*.wav'), recursive=True):
    features = extract_features(file_path)
    if features:
        data.append(features)

#create dataframe
df = pd.DataFrame(data)

#check if dataframe is empty
if df.empty:
    print("No features were extracted. Check the audio file paths or formats.")
else:
    #save the dataframe to a csv file
    output_csv_path = '/Users/cameronalevy/PycharmProjects/miso/Audio Files/CSV Directories/audio_analysis.csv'
    df.to_csv(output_csv_path, index=False)
    print(f"Features extracted and saved to {output_csv_path}")