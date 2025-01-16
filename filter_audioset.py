import pandas as pd
import os

# File path to the balanced_train_segments.csv
file_path = "/Users/cameronalevy/Documents/research miso/audio clips/balanced_train_segments.csv"

# Load the dataset, skipping malformed rows
metadata = pd.read_csv(file_path, comment="#", header=None, on_bad_lines="skip")

# Dynamically assign column names based on the number of columns
num_columns = metadata.shape[1]
column_names = ["YouTubeID", "Start", "End"] + [f"Labels{i}" for i in range(1, num_columns - 2)]
metadata.columns = column_names

# Consolidate all label columns into a single column
metadata["AllLabels"] = metadata.iloc[:, 3:].apply(
    lambda x: ", ".join(filter(pd.notnull, x)), axis=1
)

# Define misophonic-related ontology IDs and labels
target_labels = {
   # "/m/0ytgt": "Sniffling",
    #"/m/03fwl": "Chewing",
   # "/m/012xff": "Lip Smacking",
    #"/m/09x0r": "Gum (chewing gum)",
    #"/m/05b4f": "Typing",
    "/t/dd00038": "Rain on Surface"
}

# source: from google audioset ontology
#
# https://github.com/audioset/ontology/blob/master/ontology.json

# {
#    "id": "/t/dd00038",
#    "name": "Rain on surface",
#    "description": "Steady sound of many rain drops striking a surface such as a roof or window.",
#    "citation_uri": "",
#    "positive_examples": ["youtu.be/1r0Y4VFXrmE?start=30&end=40", "youtu.be/1C7lFCTvd6U?start=30&end=40",
#                          "youtu.be/0j9XJr31TA4?start=24&end=34"],
#    "child_ids": [],
#    "restrictions": []
# },


# Output directory for the filtered files
output_dir = "/Users/cameronalevy/Documents/research miso/audio clips/FilteredClips"
os.makedirs(output_dir, exist_ok=True)

# Filter and save metadata for each label
for label, label_name in target_labels.items():
    # Filter clips containing the current label
    filtered_metadata = metadata[metadata["AllLabels"].str.contains(label, na=False)]

    # Save the filtered metadata to a CSV file
    output_path = os.path.join(output_dir, f"{label_name}_clips.csv")
    filtered_metadata.to_csv(output_path, index=False)

    print(f"Filtered metadata for {label_name} saved successfully at: {output_path}")
