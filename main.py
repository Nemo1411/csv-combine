import os
import pandas as pd

def combine_csv_files(input_folder, output_file):
    # Initialize a list to store DataFrames
    data_frames = []

    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv'):
            file_path = os.path.join(input_folder, file_name)
            # Read the CSV file and add it to the list
            df = pd.read_csv(file_path)
            data_frames.append(df)

    # Combine all DataFrames into one
    combined_df = pd.concat(data_frames)

    # Remove duplicate rows
    combined_df.drop_duplicates(inplace=True)

    # Save the combined DataFrame to an output CSV file
    combined_df.to_csv(output_file, index=False)

# Use the function
input_folder = 'path/to/your/folder'  # Replace with the path to your folder containing CSV files
output_file = 'path/to/your/output/combined_file.csv'  # Replace with the path to your output CSV file

combine_csv_files(input_folder, output_file)
