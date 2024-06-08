import pandas as pd
import glob
import os

columns_of_interest = ['standar', 'complexity', 'modality', 'article', 'section', 'paragraph', 'criteria', 'cumply', 'applys']

def read_and_extract_csv(file_path, service_id):
    df = pd.read_csv(file_path, usecols=columns_of_interest)
    df['service_id'] = service_id
    cols = ['service_id'] + columns_of_interest
    df = df[cols]
    return df

csv_directory = 'csv/'  
json_directory = 'json/'  

if not os.path.exists(json_directory):
    os.makedirs(json_directory)

csv_files = glob.glob(os.path.join(csv_directory, "*.csv"))

all_data = []

for service_id, file in enumerate(csv_files, start=2):
    data = read_and_extract_csv(file, service_id)
    
    all_data.append(data)

combined_data = pd.concat(all_data, ignore_index=True)

combined_json_path = os.path.join(json_directory, 'combined_data.json')

combined_data.to_json(combined_json_path, orient='records', lines=True)

print(f"saved to {combined_json_path}.")
