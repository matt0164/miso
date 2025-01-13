import pandas as pd
import os
import subprocess

# Path to the directory containing filtered CSV files
csv_dir = "/Users/cameronalevy/Documents/research miso/audio clips/FilteredClips"
output_dir = "/Users/cameronalevy/Documents/research miso/audio clips/Clips"
os.makedirs(output_dir, exist_ok=True)

# List all filtered CSV files
csv_files = [f for f in os.listdir(csv_dir) if f.endswith("_clips.csv")]

# Download clips for each file
for csv_file in csv_files:
    csv_path = os.path.join(csv_dir, csv_file)
    data = pd.read_csv(csv_path)
    label = csv_file.replace("_clips.csv", "")

    # Create a subdirectory for the label
    label_dir = os.path.join(output_dir, label)
    os.makedirs(label_dir, exist_ok=True)

    for index, row in data.iterrows():
        youtube_id = row['YouTubeID']
        start_time = row['Start']
        end_time = row['End']

        # Construct the video URL
        video_url = f"https://www.youtube.com/watch?v={youtube_id}"

        # Set output file name
        output_file = os.path.join(label_dir, f"{youtube_id}_{start_time}-{end_time}.mp3")

        # yt-dlp command to download the clip
        command = [
            "yt-dlp",
            video_url,
            "--format", "bestaudio/best",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", output_file,
            "--postprocessor-args", f"ffmpeg:-ss {start_time} -to {end_time}"
        ]

        print(f"Downloading {output_file}...")
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {video_url}: {e}")
            continue

print("All clips downloaded successfully.")
