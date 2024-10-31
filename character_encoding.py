import pandas as pd 
import numpy as np 

import charset_normalizer

np.random.seed(0)

before = 'Строка с текстом'

print(type(before)) #<class 'str'>

after = before.encode("utf8", errors="replace")

print(type(after))
print(after)

print(after.decode("utf8"))

with open("../input/kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata:
    result = charset_normalizer.detect(rawdata.read(10000))

print(result)

kickstarter_2016 = pd.read_csv("../input/kickstarter-projects/ks-projects-201612.csv", encoding='Windows-1252')

kickstarter_2016.head()

