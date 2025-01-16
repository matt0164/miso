
import subprocess
# from dotenv import load_dotenv
# import os

#load_dotenv()
#username = os.getenv("YT_USERNAME")
#password = os.getenv("YT_PASSWORD")

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=yIQd2Ya0Ziw"

# Output directory and file name
output_file = "/Users/cameronalevy/Documents/research miso/audio clips/Clips/control/rain_on_surface.mp3"

# Your YouTube credentials
#username = os.getenv("YT_USERNAME")
#password = os.getenv("YT_PASSWORD")

# yt-dlp command to download audio
command = [
    "yt-dlp",
    video_url,
    #"--username", username,
    #"--password", password,
    "--extract-audio",
    "--audio-format", "mp3",
    "--output", output_file,
    "--cookies", "/Users/cameronalevy/Documents/research miso/www.youtube.com_cookies.txt"
]

# yt-dlp command to download entire video
# command = [
#    "yt-dlp",
#    video_url,
#    "--output", "/Users/cameronalevy/Documents/research miso/audio clips/Clips/control/rain_on_surface.%(ext)s",
#    "--cookies-from-browser", "chrome"
# ]


# yt-dlp command to download the clip
# The errors in the download script are caused by YouTube requiring authentication to confirm that you’re not a bot.
#
# To resolve the issue:
#
# Pass YouTube Cookies to yt-dlp: Export your YouTube cookies from your browser and provide them to yt-dlp using the --cookies argument. Follow these steps:
# Use a browser extension like "EditThisCookie" or another cookie-exporting tool to export cookies while logged into YouTube.
# Save the cookies to a file, e.g., cookies.txt.
# Update the download_clips.py script to include:

# Run the command
print(f"Downloading audio from: {video_url}")
try:
    subprocess.run(command, check=True)
    print(f"Audio downloaded successfully to: {output_file}")
except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
