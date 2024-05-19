import numpy as np
import os
import re
import tqdm

#%%
def numerical_sort(value):
    """
    Helper function to sort file names numerically.
    """
    parts = re.split(r'(\d+)', value)
    return [int(part) if part.isdigit() else part for part in parts]

def walk_through_and_load_files(directory):
    file_paths = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.npz'):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    # Sort files numerically
    file_paths.sort(key=numerical_sort)
    
    _data = []
    ii = 0
    for file_path in tqdm.tqdm(file_paths):
        # print(file_path)
        
        _data.append(np.load(file_path)['my_array'])

    return _data

directory_to_walk = r'masks'
walk_through_and_load_files(directory_to_walk)
