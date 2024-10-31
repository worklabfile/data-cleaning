import pandas as pd 
import numpy as np 

from scipy import stats

from mlxtend.preprocessing import minmax_scaling

import seaborn as sns
import matplotlib.pyplot as plt 

#будут генерироваться одни и те же случайные значения

np.random.seed(0)

#создаем 1000 случайных точек

original_data = np.random.exponential(size = 1000)

#распределение данных в диапазоне от 0 до 1

scaled_data = minmax_scaling(original_data, columns=[0])

#приведение к нормальному распределению

normalized_data = stats.boxcox(original_data)

#построим три графика: изначальный, в диапазоне от 0 до 1, и приведенный к нормальному распределению

fig, ax = plt.subplots(1,3,figsize=(15,3))
sns.histplot(original_data, ax=ax[0], kde= True, legend=False)
ax[0].set_title('Оригинальные данные')
sns.histplot(scaled_data, ax=ax[1], kde= True, legend=False)
ax[1].set_title('Scaling data') 
sns.histplot(normalized_data, ax=ax[2], kde= True, legend=False)
ax[2].set_title('Приведенные к нормальному распределению') #приведеное к нормальному распределению
plt.show()




