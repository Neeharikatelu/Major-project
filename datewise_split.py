#Importing the required packages
import os
import pandas as pd
from os.path import exists

#Base directory path
base = r"D:\Desktop\SEM 7\Mini Project\timestamp_out"

#Output directory path
output = r"D:\Desktop\SEM 7\Mini Project\CSV_day_output"

directory = base

#Iterate over all files in directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    print(f)
    
    try:
        # Read csv file from dataframe
        df = pd.read_csv(f)

    
        #Get unique timestamps from date columns
        dates = df['diffTimeStamp'].astype(str).str[:12].unique()
        
        #Iterate over all dates
        for d in dates:
            formatted_date = d.replace(" ", "_").replace(":", "-")
            fname = formatted_date + ".csv"
            
            #Slice the data of particular date
            df2 = df[df['diffTimeStamp'].astype(str).str[:12] == d]
            new_directory = output
            f_path = os.path.join(new_directory, fname)
            file_exists = exists(f_path)
            
            #Save to file if not exists
            if file_exists:
                df2.to_csv(f_path, mode='a', index=False, header=False)
            
            #Or append to already existing file
            else:
                df2.to_csv(f_path, index=False)
            print("written to file: ", f_path)
    except FileNotFoundError:
        print("File not found:", f)
    except PermissionError:
        print("Permission denied to write to output directory:", output)
    except Exception as e:
        print("An error occurred:", e)