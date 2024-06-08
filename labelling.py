import os
import pandas as pd
import json

# Dictionary to give labels for each hash key
hashdict = {}
hashdict_1 = {}

# ID variable to start labeling with 0
id = 1
id_1 = 1

# Base directory path
base = r"D:\Desktop\SEM 7\Mini Project\CSV_day_output"

# Output directory path
output = r"D:\Desktop\SEM 7\Mini Project\labelling"

directory = base

# Iterate over all files in the directory
for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)

    # Read a csv file to pandas dataframe
    df = pd.read_csv(f)

    # Two new columns for from and to label
    df['fromLabel'] = ''
    df['toLabel'] = ''
    df['tokenAddressLabel']=''

    # Iterate over all the rows in dataframe
    for i in range(len(df['from'])):
        if df.loc[i, 'from'] in hashdict:
            df.loc[i, 'fromLabel'] = hashdict[df.loc[i, 'from']]
        else:
            hashdict[df.loc[i, 'from']] = id
            df.loc[i, 'fromLabel'] = hashdict[df.loc[i, 'from']]
            id += 1

        if df.loc[i, 'to'] in hashdict:
            df.loc[i, 'toLabel'] = hashdict[df.loc[i, 'to']]
        else:
            hashdict[df.loc[i, 'to']] = id
            df.loc[i, 'toLabel'] = hashdict[df.loc[i, 'to']]
            id += 1
        
    for i in range(len(df['tokenAddressLabel'])):
        if df.loc[i, 'tokenAddress'] in hashdict_1:
            df.loc[i, 'tokenAddressLabel'] = hashdict_1[df.loc[i, 'tokenAddress']]
        else:
            hashdict_1[df.loc[i, 'tokenAddress']] = id_1
            df.loc[i, 'tokenAddressLabel'] = hashdict_1[df.loc[i, 'tokenAddress']]
            id_1 += 1
    # Extract only these columns
    df2 = df[['diffTimeStamp','fromLabel','toLabel','tokenAddressLabel']]
    new_directory = output
    f = os.path.join(new_directory, filename)
    print("updated ", f)

    # Save to new csv file
    df2.to_csv(f, index=False)

# with open('/home/vasundhara/Desktop/pradeep/Dictionary/NodeDict.json', 'w') as convert_file:
#     convert_file.write(json.dumps(hashdict))