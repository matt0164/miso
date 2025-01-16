import pandas as pd
import os
import subprocess

# Path to the directory containing filtered CSV files
csv_dir = "/Users/cameronalevy/Documents/research miso/audio clips/FilteredClips"
output_dir = "/Users/cameronalevy/Documents/research miso/audio clips/Clips"
os.makedirs(output_dir, exist_ok=True)

# List all filtered CSV files
# Only process the Rain_clips.csv file
csv_files = ["Rain on Surface_clips.csv"]

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
        # The errors in the download script are caused by YouTube requiring authentication to confirm that you’re not a bot.
        #
        # To resolve the issue:
        #
        # Pass YouTube Cookies to yt-dlp: Export your YouTube cookies from your browser and provide them to yt-dlp using the --cookies argument. Follow these steps:
        # Use a browser extension like "EditThisCookie" or another cookie-exporting tool to export cookies while logged into YouTube.
        # Save the cookies to a file, e.g., cookies.txt.
        # Update the download_clips.py script to include:

        command = [
            "yt-dlp",
            video_url,
            "--format", "bestaudio/best",
            "--extract-audio",
            "--audio-format", "wav",
            "--output", output_file,
            "--postprocessor-args", f"ffmpeg:-ss {start_time} -to {end_time}"
            "--cookies", "path/to/cookies.txt" #this is a new line to pass the cookies from browser to prevent bot blocking
        ]

        print(f"Downloading {output_file}...")
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {video_url}: {e}")
            continue

print("All clips downloaded successfully.")
