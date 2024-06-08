import pandas as pd
import time
import csv
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

# Iterate over all files in the input directory
for filename in os.listdir(base):
    f = os.path.join(base, filename)

    # Read the CSV file using the absolute path
    df = pd.read_csv(f)

    # Apply the time_format function to the 'timestamp' column
    df['diffTimeStamp'] = df['timestamp'].apply(time_format)

    # Reorder the columns
    df = df.reindex(columns=['blockNumber', 'timestamp','diffTimeStamp', 'transactionHash', 'tokenAddress', 'from', 'to', 'fromIsContract', 'toIsContract', 'tokenId'])

    # Define the new file path in the output directory
    new_filename = os.path.splitext(filename)[0] + '.csv'
    new_filepath = os.path.join(output_directory, new_filename)

    # Save the modified CSV file to the output directory
    df.to_csv(new_filepath, index=False)
