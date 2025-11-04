 import pandas as pd


 import numpy as np
 data = pd.read_html('fatal-police-shootings-data(1).csv', header=0)
 table = pd.DataFrame(data[0])
 table.rename(columns = {'name': 'IMIĘ', 'data': 'DATA', 'manner of death': 'SPOSÓb ŚMIERCI', 'armed':'uzbrojony',} inplace = True)
 table.head()

illness_dict = dict(zip(df['race'].unique(),[]))

 df['sign_of_mental_illness'] = df['race '].map
 df[day_of_week ]= df['Interwencje'].apply(lambda x: day_of_week(x))
 chart_set_axis({
    'name':'x^2'
    'day_of_week':{'day': Monday, 'Interwencja': True}

 })
 data = pd.read_csv('dane dotyczące populacji w poszczególnych stanach USA')
 data = pd.read_csv(' dane dotyczące skrótów poszczególnych stanów.')




