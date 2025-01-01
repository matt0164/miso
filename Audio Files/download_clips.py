import pandas as pd
import os
import subprocess

# Path to the CSV file (adjusted for your structure)
csv_file = "C:/Users/matt0/PycharmProjects/miso/Audio Files/CSV Directories/filtered_audioset_clips.csv"
output_dir = "Audio Files/Clips"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the CSV
data = pd.read_csv(csv_file)

# Iterate over rows and download clips
for index, row in data.iterrows():
    youtube_id = row['YouTubeID']
    start_time = row['Start']
    end_time = row['End']

    # Construct the video URL
    video_url = f"https://www.youtube.com/watch?v={youtube_id}"

    # Set output file name
    output_file = os.path.join(output_dir, f"{youtube_id}_{start_time}-{end_time}.mp3")

    # yt-dlp command to download the clip
    command = [
        "C:/Users/matt0/anaconda3/Scripts/yt-dlp.exe",
        video_url,
        "--format", "bestaudio/best",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", output_file,
        "--postprocessor-args", f"ffmpeg:-ss {start_time} -to {end_time}",
        "--ffmpeg-location", "C:/Program Files (x86)/ffmpeg-master-latest-win64-gpl/bin",
        "--force-overwrites"
    ]

    # Run the command
    print(f"Downloading {output_file}...")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {video_url}: {e}")
        continue

print("All clips downloaded successfully.")
