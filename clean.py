import pandas as pd 
import numpy as np 

nfl_data = pd.read_csv('scv/NFL Play by Play 2009-2017 (v4).csv')

# print(nfl_data.columns)

# print(nfl_data.head())

missing_values_count = nfl_data.isnull().sum()

total_cells = nfl_data.size

print(missing_values_count.sum()/total_cells*100)

print(missing_values_count[0:10])


