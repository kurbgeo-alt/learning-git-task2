In [1]: import pandas as pd

   ...: import numpy as np


In [2]: data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)


In [3]: table = pd.DataFrame(data[0])


In [4]: table.rename(columns={'POS': 'POZ', 'TITLE': 'TYTUŁ', 'ARTIST': 'ARTYSTA', 'YEAR': 'ROK', 'HIGH POSN': 'MAX POZ'}, inplace = True)


In [5]: table.head()

Out[5]: 

POZ TYTUŁ ARTYSTA ROK MAX POZ

0 1 GREATEST HITS QUEEN 1981 1

1 2 GOLD - GREATEST HITS ABBA 1992 1

2 3 SGT PEPPER'S LONELY HEARTS CLUB BAND BEATLES 1967 1

3 4 21 ADELE 2011 1

4 5 WHAT'S THE STORY MORNING GLORY OASIS 1995 1


In [6]: artist = table['ARTYSTA'].nunique()

   ...: artist

Out[6]: 47


In [7]: Zespoły najczęściej pojawiające się

Cell In[7], line 1

Zespoły najczęściej pojawiające się

^

SyntaxError: invalid syntax



In [8]: artist_top = table['ARTYSTA'].value_counts().head()


In [9]: artist_top

Out[9]: 

ARTYSTA

COLDPLAY 3

TAKE THAT 3

FLEETWOOD MAC 2

ABBA 2

DIDO 2

Name: count, dtype: int64


In [10]: table.rename(str.capitalize, axis='columns', inplace = True)

    ...: table.head()

Out[10]: 

Poz Tytuł Artysta Rok Max poz

0 1 GREATEST HITS QUEEN 1981 1

1 2 GOLD - GREATEST HITS ABBA 1992 1

2 3 SGT PEPPER'S LONELY HEARTS CLUB BAND BEATLES 1967 1

3 4 21 ADELE 2011 1

4 5 WHAT'S THE STORY MORNING GLORY OASIS 1995 1


In [11]: table.drop(columns = 'Max poz', inplace = True)


In [12]: table.head()

Out[12]: 

Poz Tytuł Artysta Rok

0 1 GREATEST HITS QUEEN 1981

1 2 GOLD - GREATEST HITS ABBA 1992

2 3 SGT PEPPER'S LONELY HEARTS CLUB BAND BEATLES 1967

3 4 21 ADELE 2011

4 5 WHAT'S THE STORY MORNING GLORY OASIS 1995


In [13]: table_y_max = table['Rok'].value_counts()

    ...: table_y_max.head()

Out[13]: 

Rok

2000 4

1987 4

2006 3

1977 3

1998 3

Name: count, dtype: int64


In [14]: t_60_90 = table[(table['Rok'] >= 1960) & (table['Rok'] <= 1990)]['Rok']

    ...: t_60_90.count()

Out[14]: np.int64(22)


In [15]: table[table['Rok'] == max(table['Rok'])]

Out[15]: 

Poz Tytuł Artysta Rok

26 27 25 ADELE 2015


In [16]: artist_first_on_top = table.groupby('Artysta').agg({'Tytuł':'first','Rok':'min'})


In [17]: artist_first_on_top.sort_values('Rok').head()

Out[17]: 

Tytuł Rok

Artysta 

ORIGINAL CAST RECORDING THE SOUND OF MUSIC 1965

BEATLES SGT PEPPER'S LONELY HEARTS CLUB BAND 1967

SIMON & GARFUNKEL BRIDGE OVER TROUBLED WATER 1970

PINK FLOYD THE DARK SIDE OF THE MOON 1973

MIKE OLDFIELD TUBULAR BELLS 1973


In [18]: list_to_excel = artist_first_on_top.sort_values('Rok')


In [19]: list_to_excel.to_csv('ArtistFirstOnTop.csv', index=False)


In [20]: 