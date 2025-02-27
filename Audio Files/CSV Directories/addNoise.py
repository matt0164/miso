import os
import librosa
import soundfile as sf

# Folder containing audio files
input_folder = '/Users/cameronalevy/Documents/research miso/audio clips/Clips'
output_folder = '/Users/cameronalevy/Documents/research miso/audio clips/withNoise'

# Process all files in folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)

    if not file_name.lower().endswith('.wav'):
        continue

    try:
        y, sr = librosa.load(file_path, sr=None)
        # Apply augmentations
        y_aug = librosa.effects.pitch_shift(y, sr=sr, n_steps=2)
        y_aug = librosa.effects.time_stretch(y_aug, rate=1.1)
        sf.write(os.path.join(output_folder, "aug_" + file_name), y_aug, sr)
        print(f"processed {file_name}")

    except Exception as e:
        print(f"error processing {file_name}: {e}")