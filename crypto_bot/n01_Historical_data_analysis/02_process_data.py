import pandas as pd
import os
from utils.indicators import add_indicators  # Import add_indicators from the utils package

# Define input and output folders
INPUT_FOLDER = "data"               # Folder containing raw data
OUTPUT_FOLDER = "data/processed"    # Folder to save processed data

# Ensure the processed folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each data file in the input folder
for file in os.listdir(INPUT_FOLDER):
    if file.endswith(".csv"):
        print(f"Processing {file}...")

        # Load the data
        file_path = os.path.join(INPUT_FOLDER, file)
        data = pd.read_csv(file_path)

        # Add indicators to the data
        data = add_indicators(data)

        # Save the processed data
        output_path = os.path.join(OUTPUT_FOLDER, file)
        data.to_csv(output_path, index=False)
        print(f"Saved processed data to {output_path}")
