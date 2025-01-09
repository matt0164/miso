# this script will remove all failed or corrupt files.
# It will ask the user for the paths to the failed_files.txt and the dataset (audio clips) folder.

import os

def delete_failed_files(failed_files_path, dataset_folder):
    try:
        # Read the failed files list
        with open(failed_files_path, "r") as file:
            failed_files = file.read().splitlines()

        # Delete each failed file
        for failed_file in failed_files:
            file_path = os.path.join(dataset_folder, os.path.basename(failed_file))
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")

        print("Failed file cleanup complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt user for paths with sample paths included in the message
    failed_files_path = input("Enter the path to 'failed_files.txt' (e.g., C:\\Users\\matt0\\PycharmProjects\\miso\\Audio Files\\Audio Files\\failed_files.txt): ").strip()
    dataset_folder = input("Enter the path to the dataset folder (e.g., C:\\Users\\matt0\\PycharmProjects\\miso\\Audio Files\\Audio Files\\Clips): ").strip()

    # Run the cleanup
    delete_failed_files(failed_files_path, dataset_folder)
