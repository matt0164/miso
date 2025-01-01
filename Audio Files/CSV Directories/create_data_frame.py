import pandas as pd
import os

# Paths
file_path = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\balanced_train_segments.csv"
output_dir = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\Audio Files\Clips"  # Corrected directory
filtered_csv = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\filtered_audioset_clips.csv"
valid_csv = r"C:\Users\matt0\PycharmProjects\miso\Audio Files\CSV Directories\valid_audioset_clips.csv"

# Load the full dataset
metadata = pd.read_csv(file_path, comment="#", header=None, on_bad_lines="skip")

# Dynamically assign column names
num_columns = metadata.shape[1]
column_names = ["YouTubeID", "Start", "End"] + [f"Labels{i}" for i in range(1, num_columns - 2)]
metadata.columns = column_names

# Consolidate all label columns into a single column
metadata["Labels"] = metadata.iloc[:, 3:].apply(
    lambda x: ", ".join(filter(pd.notnull, x)), axis=1
)

# Define misophonia-related ontology IDs
target_labels = ["/m/09x0r", "/m/03fwl", "/m/012xff"]

# Filter clips containing target labels
filtered_metadata = metadata[metadata["Labels"].str.contains("|".join(target_labels), na=False)]
filtered_metadata = filtered_metadata.copy()  # Avoid SettingWithCopyWarning

# Save the filtered dataset
filtered_metadata.to_csv(filtered_csv, index=False)
print(f"Filtered metadata saved at: {filtered_csv}")

# Check files in Clips directory
clip_files = os.listdir(output_dir)
print(f"Files in Clips directory: {clip_files[:10]}")  # Debug: Show a sample of files

# Add ClipPath and check if files exist
for index, row in filtered_metadata.iterrows():
    youtube_id = row['YouTubeID']
    start_time = f"{float(row['Start']):.1f}"  # Always include one decimal place
    end_time = f"{float(row['End']):.1f}"

    # Construct the expected clip path
    clip_path = os.path.join(output_dir, f"{youtube_id}_{start_time}-{end_time}.mp3")
    exists = os.path.exists(clip_path)

    # Debug: Print constructed path and closest matches
    print(f"Checking: {clip_path} - Exists: {exists}")
    closest_matches = [file for file in clip_files if youtube_id in file]
    print(f"Closest matches in directory: {closest_matches}")

    filtered_metadata.loc[index, 'ClipPath'] = clip_path if exists else None

# Filter for rows where the audio file exists
valid_clips = filtered_metadata[filtered_metadata['ClipPath'].notnull()]
print(f"Number of valid clips: {len(valid_clips)}")

# Save the final valid dataset
valid_clips.to_csv(valid_csv, index=False)
print(f"Filtered dataset with valid audio files saved at: {valid_csv}")
