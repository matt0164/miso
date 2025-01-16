# This script processes a dataset by reading all valid files from a folder, dynamically assigning column names,
# consolidating labels into a single DataFrame, and saving the processed data to a CSV file.

# A DataFrame is a 2-dimensional labeled data structure provided by the pandas library, similar to a table in a database.
# It allows easy manipulation, analysis, and visualization of structured data.

import os
import pandas as pd

def load_and_process_dataset(dataset_folder):
    """
    Loads and processes all valid dataset files in a given folder.

    Parameters:
        dataset_folder (str): Path to the folder containing the dataset files.

    Returns:
        pd.DataFrame: A consolidated DataFrame with data from all valid files.
    """
    try:
        # Get all CSV files in the dataset folder
        files = [f for f in os.listdir(dataset_folder) if f.endswith(".csv")]

        # Initialize an empty DataFrame
        combined_data = pd.DataFrame()

        for file in files:
            file_path = os.path.join(dataset_folder, file)
            try:
                # Load data and dynamically assign column names
                data = pd.read_csv(file_path, encoding="utf-8")  # Handle proper encoding
                column_names = [f"feature_{i}" for i in range(data.shape[1])]
                data.columns = column_names

                # Consolidate label columns into a single frame (adjust as needed)
                if "label" in data.columns:
                    combined_data = pd.concat([combined_data, data], ignore_index=True)
                else:
                    print(f"No 'label' column in {file}, skipping...")

            except Exception as file_error:
                print(f"Error reading file {file_path}: {file_error}")

        print("Data processing complete.")
        return combined_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Default paths
    # for mac need to adjust and replace with your path
    # for mac - standard format is : /Users/<your-username>/Desktop/miso audio/balanced_train_segments.csv

    default_dataset_folder = "/Users/cameronalevy/Documents/research miso/audio clips/clips"
    default_output_file = "/Users/cameronalevy/Documents/research miso/audio clips/processed_dataset.csv"

    # Prompt user for paths with option to use defaults
    dataset_folder = input(f"Enter the path to the cleaned dataset folder (default: {default_dataset_folder}): ").strip()
    if not dataset_folder:
        dataset_folder = default_dataset_folder

    output_file = input(f"Enter the path to save the processed dataset (default: {default_output_file}): ").strip()
    if not output_file:
        output_file = default_output_file

    # Load and process dataset
    processed_data = load_and_process_dataset(dataset_folder)

    # Save the processed data as a CSV
    if processed_data is not None:
        processed_data.to_csv(output_file, index=False)
        print(f"Processed dataset saved as '{output_file}'.")
