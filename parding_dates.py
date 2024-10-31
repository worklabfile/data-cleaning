import pandas as pd 
import numpy as np 

import seaborn as sns
import datetime 

np.random.seed(0)

landsides = pd.read_csv("csv/catalog.csv")

# print(landsides['date'].head())

landsides['date_parsed'] = pd.to_datetime(landsides['date'], format="%m/%d/%y")

print(landsides['date_parsed'].head())

month_of_lansides = landsides['date_parsed'].dt.month

month_of_lansides = month_of_lansides.dropna()

sns.displot(month_of_lansides, kde = False, bins = 12)