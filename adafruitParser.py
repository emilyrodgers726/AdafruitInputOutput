import pandas as pd
import json
import os

def hex_to_string(hex_data):
    """
    Convert hexadecimal string to ASCII text.
    
    Args:
        hex_data (str): A string of hexadecimal characters.
    
    Returns:
        str: The ASCII representation of the hexadecimal input.
    """
    
    bytes_object = bytes.fromhex(hex_data)
    return bytes_object.decode("ASCII")

def process_csv(input_csv_path, output_folder):
    """
    Processes a CSV file: sorts by date, converts HEX values in 'value' column to text, 
    and saves each row as an individual JSON file.
    
    Args:
        input_csv_path (str): The file path to the input CSV.
        output_folder (str): The directory where output JSON files will be saved.
    """

    print(f"Processing CSV file: {input_csv_path}. Please hold...")

    # Load the CSV
    data = pd.read_csv(input_csv_path)

    # Sort data by 'created_at'
    data_sorted = data.sort_values(by='created_at')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each row, convert HEX to text, and save to JSON file
    for index, row in enumerate(data_sorted.itertuples(), start=1):
        decoded_value = hex_to_string(row.value)
        value_json = json.loads(decoded_value)  # Convert the decoded string to a JSON object
        json_data = {
            "created_at": row.created_at,
            **value_json  # Merge the decoded JSON object into the main JSON structure
        }
        output_filename = os.path.join(output_folder, f"output{index:06d}.json")
        with open(output_filename, 'w') as f:
            json.dump(json_data, f, indent=4)

    print(f"Processed {index} entries, files saved in {output_folder}")

# Set your CSV input file path and output directory
input_csv_path = "/Users/emilyrodgers/jsonInputOutput/input/input.csv"
output_folder = "/Users/emilyrodgers/jsonInputOutput/output/"

# Function call to process the CSV
process_csv(input_csv_path, output_folder)