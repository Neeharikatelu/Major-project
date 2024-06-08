import pandas as pd
import time
import csv
import os

base = r"D:\Desktop\SEM 7\Mini Project\csv data"



directory = base

# Iterate over all files in directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    # Read the CSV file using a relative path if the CSV file is in the same directory as your script
    df = pd.read_csv(f)


    # Creating a function which converts the format of the timeStamp
    def time_format(timestamp):
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        return otherStyleTime

    # Picking the timeStamp column and applying the function to each row of the column.
    # Creating a new column altogether
    df['diffTimeStamp'] = df['timestamp'].apply(time_format)

    # Changing the order of the columns in the dataset
    df = df.reindex(columns=['blockNumber', 'timestamp','diffTimeStamp', 'transactionHash', 'tokenAddress', 'from', 'to', 'fromIsContract', 'toIsContract', 'tokenId'])

    # Updating and saving the CSV file with a new name
    new_filename = os.path.splitext(filename)[0] + '.csv'
    new_filepath = os.path.join(directory, new_filename)
    df.to_csv(new_filepath, index=False)
