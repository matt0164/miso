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
```python
file_path = "/Users/cameronalevy/Documents/research miso/audio clips/balanced_train_segments.csv"
output_path = "/Users/cameronalevy/Documents/research miso/audio clips/filtered_audioset_clips.csv"


## OLD:
includes PC-based filepaths and from 1/13/25 

### filtered_audio.py 
is a python script that parses the data in the data files and returns only sounds that are labeled as misphponnic (e.g. biting, chewing, etc.)
It will return a new csv file "filtered_audioset_clips.csv" from the 3 Google DataSet files.

#### In this code, you need to update the file path to the balanced_train_segments.csv and the output path here:
file_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\balanced_train_segments.csv"

output_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\filtered_audioset_clips.csv"

### download_clips.py
This script automates the process of downloading and extracting specific audio segments from YouTube videos. It uses data from the filtered_audioset_clips.csv file, which contains YouTube video IDs and the start/end timestamps for each desired clip. The script relies on yt-dlp for downloading and processes the following steps:

Input CSV: Reads the filtered_audioset_clips.csv file to get video IDs and clip timestamps.
Clip Download: Downloads the specified audio segments from YouTube using yt-dlp.
Output Directory: Saves the extracted audio files in the Audio Files/Clips folder in MP3 format.

