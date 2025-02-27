import os
import glob
import pandas as pd
import librosa
import librosa.display
from librosa import feature as lf
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import butter, sosfiltfilt

def bandpass_filter(signal, sr, lowcut=2500, highcut=5500, order=5):
    nyquist = 0.5 * sr
    low = lowcut / nyquist
    high = highcut / nyquist
    sos = butter(order, [low, high], btype='band', output='sos')
    return sosfiltfilt(sos, signal, axis=0)

audio_directory = '/Users/cameronalevy/Documents/research miso/audio clips/testClips'

data = []

#extract features from audio file
def extract_features(audio_file_path):

    try:
        y, sr = librosa.load(audio_file_path, sr=None)
        print("audio loaded")

        #extract features
        path = audio_file_path
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


        #return features as dictionary
        return {
            'path': path,
            'rms': rms,
            'zcr': zcr,
            'chroma': chroma,
            'tonnetz': tonnetz,
            "energy_2500_5500Hz": energy_2500_5500hz,
            "modulation_energy_1_16Hz": modulation_energy
        }
    except Exception as e:
        print(f"Error processing {audio_file_path}: {e}")
        return None

for file_path in glob.glob(os.path.join(audio_directory, '**', '*.wav'), recursive=True):
    features = extract_features(file_path)
    if features:
        data.append(features)

df = pd.DataFrame(data)

if df.empty:
    print("No features were extracted. Check the audio file paths or formats.")
else:
    #save the dataframe to a csv file
    output_csv_path = '/Users/cameronalevy/PycharmProjects/miso/Audio Files/CSV Directories/data.csv'
    df.to_csv(output_csv_path, index=False)
    print(f"Features extracted and saved to {output_csv_path}")
