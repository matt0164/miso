import os
import subprocess

# Path to ffmpeg executable
ffmpeg_path = r"C:\Program Files (x86)\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"

# Directory containing your audio files
audio_dir = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\Audio Files\Clips"

# File to log failed files
failed_files_log = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\Audio Files\failed_files.txt"

failed_files = []

# Iterate through all audio files and re-encode them
for file_name in os.listdir(audio_dir):
    if file_name.endswith(".mp3"):
        input_path = os.path.join(audio_dir, file_name)
        output_path = os.path.join(audio_dir, "fixed_" + file_name)
        try:
            # Run ffmpeg command to re-encode the audio file with the -y flag
            subprocess.run([
                ffmpeg_path, "-y", "-i", input_path, "-acodec", "libmp3lame", "-q:a", "2", output_path
            ], check=True)
            print(f"Re-encoded: {file_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to re-encode: {file_name}")
            failed_files.append(file_name)

# Save failed files to a log
if failed_files:
    with open(failed_files_log, "w") as f:
        f.write("\n".join(failed_files))
    print(f"Failed files logged in: {failed_files_log}")
