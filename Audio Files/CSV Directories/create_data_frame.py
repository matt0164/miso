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
        # Get all files in the dataset folder
        files = [f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]

        # Initialize an empty DataFrame
        combined_data = pd.DataFrame()

        for file in files:
            file_path = os.path.join(dataset_folder, file)
            try:
                # Load data and dynamically assign column names
                data = pd.read_csv(file_path, encoding="utf-8", errors="replace")  # Replace invalid characters
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
    # Prompt user for paths with sample paths included in the message
    dataset_folder = input("Enter the path to the cleaned dataset folder (e.g., C:\\Users\\matt0\\PycharmProjects\\miso\\Audio Files\\Audio Files\\Clips): ").strip()
    output_file = input("Enter the path to save the processed dataset (e.g., C:\\Users\\matt0\\PycharmProjects\\miso\\Audio Files\\processed_dataset.csv): ").strip()

    # Load and process dataset
    processed_data = load_and_process_dataset(dataset_folder)

    # Save the processed data as a CSV
    if processed_data is not None:
        processed_data.to_csv(output_file, index=False)
        print(f"Processed dataset saved as '{output_file}'.")
