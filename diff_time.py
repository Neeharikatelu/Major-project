import pandas as pd
import time
import os

base = r"D:\Desktop\SEM 7\Mini Project\csv data"
output_directory = r"D:\Desktop\SEM 7\Mini Project\timestamp_out"

# Create the output directory if it does not exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Function to convert the format of the timeStamp
def time_format(timestamp):
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
    return otherStyleTime

# Define a dictionary for data types
dtype_dict = {
    'blockNumber': 'int64',
    'timestamp': 'int64',
    'transactionHash': 'object',
    'tokenAddress': 'object',
    'from': 'object',
    'to': 'object',
    'fromIsContract': 'object',  # Read as object initially
    'toIsContract': 'object',    # Read as object initially
    'tokenId': 'object'          # Keep as object to handle mixed types
}

# Function to process and save a single chunk
def process_chunk(chunk, output_filepath):
    # Convert boolean columns
    chunk['fromIsContract'] = chunk['fromIsContract'].astype(bool)
    chunk['toIsContract'] = chunk['toIsContract'].astype(bool)

    # Apply the time_format function to the 'timestamp' column
    chunk['diffTimeStamp'] = chunk['timestamp'].apply(time_format)

    # Reorder the columns
    chunk = chunk.reindex(columns=['blockNumber', 'timestamp', 'diffTimeStamp', 'transactionHash', 'tokenAddress', 'from', 'to', 'fromIsContract', 'toIsContract', 'tokenId'])

    # Append to the output file
    chunk.to_csv(output_filepath, mode='a', index=False, header=not os.path.exists(output_filepath))

# Iterate over all files in the input directory
for filename in os.listdir(base):
    f = os.path.join(base, filename)

    new_filename = os.path.splitext(filename)[0] + '.csv'
    new_filepath = os.path.join(output_directory, new_filename)

    # Remove the output file if it already exists
    if os.path.exists(new_filepath):
        os.remove(new_filepath)

    # Read and process the CSV file in chunks
    try:
        chunk_size = 100000  # Adjust the chunk size based on your system's memory capacity
        for chunk in pd.read_csv(f, dtype=dtype_dict, low_memory=False, chunksize=chunk_size):
            process_chunk(chunk, new_filepath)
    except Exception as e:
        print(f"Error reading {f}: {e}")
