import pandas as pd
import os 

data = {'Name' : ['Alice','Bob','Charlie'],
        'age' : [25,30,35],
        'city' : ['New York' , 'Los Aangles','Chicago']
        }

df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir , exist_ok = True)

file_path = os.path.join(data_dir , 'simmple_dat.csv')

df.to_csv(file_path , index  = False)
print(f"csv file savded to {file_path}")