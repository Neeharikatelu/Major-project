import os
import pandas as pd
import json

# Initialize dictionaries for labeling
hashdict = {}
hashdict_1 = {}

# Initialize ID counters for labels
id = 1
id_1 = 1

# Base directory containing the CSV files
base_directory = r"D:\Desktop\SEM 7\Mini Project\CSV_day_output"

# Output directory for labeled CSV files
output_directory = r"D:\Desktop\SEM 7\Mini Project\labelling_2017"

# Iterate over all files in the base directory
for filename in sorted(os.listdir(base_directory)):
    file_path = os.path.join(base_directory, filename)

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path, low_memory=False)

    # Add new columns for labels
    df['fromLabel'] = ''
    df['toLabel'] = ''
    df['tokenAddressLabel'] = ''

    # Label 'from' and 'to' columns
    for i in range(len(df)):
        from_address = df.loc[i, 'from']
        to_address = df.loc[i, 'to']

        if from_address in hashdict:
            df.loc[i, 'fromLabel'] = hashdict[from_address]
        else:
            hashdict[from_address] = id
            df.loc[i, 'fromLabel'] = id
            id += 1

        if to_address in hashdict:
            df.loc[i, 'toLabel'] = hashdict[to_address]
        else:
            hashdict[to_address] = id
            df.loc[i, 'toLabel'] = id
            id += 1

    # Label 'tokenAddress' column
    for i in range(len(df)):
        token_address = df.loc[i, 'tokenAddress']

        if token_address in hashdict_1:
            df.loc[i, 'tokenAddressLabel'] = hashdict_1[token_address]
        else:
            hashdict_1[token_address] = id_1
            df.loc[i, 'tokenAddressLabel'] = id_1
            id_1 += 1

    # Select the relevant columns
    df_labeled = df[['diffTimeStamp', 'fromLabel', 'toLabel', 'tokenAddressLabel']]

    # Save the labeled DataFrame to the output directory
    output_file_path = os.path.join(output_directory, filename)
    df_labeled.to_csv(output_file_path, index=False)

    print(f"Updated {output_file_path}")

# Optionally, save the dictionaries to JSON files
# with open(r'D:\Desktop\SEM 7\Mini Project\Dictionary\NodeDict.json', 'w') as convert_file:
#     json.dump(hashdict, convert_file)
# with open(r'D:\Desktop\SEM 7\Mini Project\Dictionary\TokenDict.json', 'w') as convert_file:
#     json.dump(hashdict_1, convert_file)
