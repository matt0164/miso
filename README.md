# Misophonia Audio Dataset Processing

This project focuses on identifying and processing misophonic sounds (e.g., chewing, biting, lip smacking) from audio datasets. It consists of two primary Python scripts designed to filter relevant audio clips and download them for analysis.

## Features
1. **Filtering Misophonic Clips**: Parse the AudioSet metadata to isolate audio clips with labels related to misophonic triggers.
2. **Automated Audio Clip Downloads**: Download and extract specific audio segments from YouTube videos based on the filtered data.

---

## Scripts Overview

### 1. `filter_audioset.py`
This script processes the `balanced_train_segments.csv` file from the Google AudioSet dataset to extract audio clips labeled with misophonic-related categories.

#### Key Steps:
- Reads the metadata CSV and dynamically assigns column names.
- Identifies clips with specific labels (`/m/09x0r`, `/m/03fwl`, `/m/012xff` corresponding to misophonic sounds).
- Outputs a filtered CSV file: `filtered_audioset_clips.csv`.

#### Configuration:
The file paths are set up for macOS. Update these paths if needed:

- MAC:
  - file_path = "/Users/cameronalevy/Documents/research miso/audio clips/balanced_train_segments.csv"
  - output_path = "/Users/cameronalevy/Documents/research miso/audio clips/filtered_audioset_clips.csv"

- PC:
  - file_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\balanced_train_segments.csv"
  - output_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\filtered_audioset_clips.csv"

### 2. `download_clips.py`
This script automates the download of audio clips listed in `filtered_audioset_clips.csv` using the `yt-dlp` library. It extracts specific segments from YouTube videos based on timestamps.

#### Key Steps:
- Reads `filtered_audioset_clips.csv` to get YouTube video IDs and clip start/end times.
- Downloads the audio clips in MP3 format.
- Saves the extracted clips in the `Audio Files/Clips` directory.

#### Configuration:
Set the input CSV path and output directory:

- MAC:
  - csv_file = "/Users/cameronalevy/Documents/research miso/audio clips/filtered_audioset_clips.csv"
  - output_dir = "/Users/cameronalevy/Documents/research miso/audio clips/Audio Files/Clips"

- PC:
  - csv_file = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\filtered_audioset_clips.csv"
  - output_dir = "Audio Files/Clips"
    - C:\Users\matt0\PycharmProjects\miso\Audio Files\Audio Files\Clips

## Requirements
- **Python**: Ensure you have Python 3.7 or higher.
- **Libraries**: Install the following Python libraries:
  - `certifi==2024.8.30`
  - `charset-normalizer==3.3.2`
  - `idna==3.10`
  - `numpy==2.0.2`
  - `pandas==2.2.3`
  - `python-dateutil==2.9.0.post0`
  - `python-dotenv==1.0.1`
  - `pytz==2024.2`
  - `requests==2.32.3`
  - `six==1.16.0`
  - `tabulate==0.9.0`
  - `tzdata==2024.2`
- **Tools**:
  - `yt-dlp`
  - `FFmpeg`

- **Install dependencies** using bash:
    - pip install -r requirements.txt

