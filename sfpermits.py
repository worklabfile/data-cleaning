import pandas as pd 
import numpy as np

sf_permits = pd.read_csv("csv/Building_Permits.csv")

print(sf_permits.head())

print(sf_permits.isnull().sum().sum()/sf_permits.size)

total_cells = np.product(sf_permits.shape)

total_missing = sf_permits.sum().sum()

print(total_cells/total_missing)

print(sf_permits.shape[1]-sf_permits.dropna().shape[1])