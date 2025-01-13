
import pandas as pd

#File path to the balanced_train_segments.csv
file_path = "/Users/cameronalevy/Documents/research miso/audio clips/balanced_train_segments.csv"

#Load the dataset, skipping malformed rows
metadata = pd.read_csv(file_path, comment="#", header=None, on_bad_lines="skip")

#Dynamically assign column names based on the number of columns
num_columns = metadata.shape[1]
column_names = ["YouTubeID", "Start", "End"] + [f"Labels{i}" for i in range(1, num_columns - 2)]
metadata.columns = column_names

#Consolidate all label columns into a single column
metadata["AllLabels"] = metadata.iloc[:, 3:].apply(
    lambda x: ", ".join(filter(pd.notnull, x)), axis=1
)

#Define misophonic-related ontology IDs
target_labels = ["/m/09x0r", "/m/03fwl", "/m/012xff"]  # Replace with IDs for "chewing", "biting", "lip smacking"

#Filter clips containing target labels
filtered_metadata = metadata[metadata["AllLabels"].str.contains("|".join(target_labels), na=False)]

#Output path for the filtered metadata
output_path = "/Users/cameronalevy/Documents/research miso/audio clips/filtered_audioset_clips.csv"

#Save the filtered metadata to a CSV file
filtered_metadata.to_csv(output_path, index=False)

print(f"Filtered metadata saved successfully at: {output_path}")
