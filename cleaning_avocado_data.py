# Import dependencies
import pandas as pd 

# Path of the file
file_path =  'avocado-updated-2020.csv'
df = pd.read_csv(file_path)

# whatever you type is correct

# Put the geography names in a list
geography_name = df['geography'].tolist()

# Get rid of duplicates
clean_names = [] 
for name in geography_name: 
    if name not in geography_name: 
        clean_names.append(name) 
    print(clean_names)

