# miso

filtered_audio.py is a python script that parses the data in the data files and returns only sounds that are labeled as misphponnic (e.g. biting, chewing, etc.)
It will return a new csv file "filtered_audioset_clips.csv" from the 3 Google DataSet files.

# In this code, you need to update the file path to the balanced_train_segments.csv here:
file_path = r"C:\Users\matt0\OneDrive\Documents\00 Matt\Coding\sound files\balanced_train_segments.csv"

# And you can define misophonic-related ontology IDs by updating this code:
target_labels = ["/m/09x0r", "/m/03fwl", "/m/012xff"]  # Replace with IDs for "chewing", "biting", "lip smacking"

# And you need to update the output path for the filtered metadata here:
output_path = r"C:\Users\matt0\OneDrive\Documents\00 Matt\Coding\sound files\filtered_audioset_clips.csv"
