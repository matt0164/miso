# miso

## filtered_audio.py 
is a python script that parses the data in the data files and returns only sounds that are labeled as misphponnic (e.g. biting, chewing, etc.)
It will return a new csv file "filtered_audioset_clips.csv" from the 3 Google DataSet files.

### In this code, you need to update the file path to the balanced_train_segments.csv and the output path here:
file_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\balanced_train_segments.csv"

output_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\filtered_audioset_clips.csv"

## download_clips.py
This script automates the process of downloading and extracting specific audio segments from YouTube videos. It uses data from the filtered_audioset_clips.csv file, which contains YouTube video IDs and the start/end timestamps for each desired clip. The script relies on yt-dlp for downloading and processes the following steps:

Input CSV: Reads the filtered_audioset_clips.csv file to get video IDs and clip timestamps.
Clip Download: Downloads the specified audio segments from YouTube using yt-dlp.
Output Directory: Saves the extracted audio files in the Audio Files/Clips folder in MP3 format.