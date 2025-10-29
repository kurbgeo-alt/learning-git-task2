In [4]: import pandas as pd


In [5]: import numpy as np


In [6]: data = pd.read_html('fatal-police-shootings-data(1).csv', header=0)
In[7]: table = pd.DataFrame(data[0])
In table.rename(columns = {'name': 'IMIĘ', 'data': 'DATA', 'manner of death': 'SPOSÓb ŚMIERCI', 'armed':'uzbrojony',} inplace = True)
In table.head()
In [8]: sign_of_mental_illness_dict =dict(zip('race').unique(),

   ...: df

   ...: 

   ...: 

   ...: 

   ...: 

   ...: 

   ...: df{'fatal_police-shootings-data(1).csv') = df('race').map(sign_of_mental_illness_dict)

Cell In[8], line 8

df{'fatal_police-shootings-data(1).csv') = df('race').map(sign_of_mental_illness_dict)

