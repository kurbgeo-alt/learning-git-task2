import pandas as pd
import numpy as np



data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/', header=0)

table = pd.DataFrame(data[0])


table.rename(columns={'POS': 'POZ', 'TITLE': 'TYTUŁ', 'ARTIST': 'ARTYSTA', 'YEAR': 'ROK', 'HIGH POSN': 'MAX POZ'}, inplace = True)


table.head()
print(table.head())
print("Zamiana nagłówków kolumn na polskie odpowiedniki")




artist = table['ARTYSTA'].nunique()
print(artist)

print("Liczba  pojedynczych artystów")




artist_top = table['ARTYSTA'].value_counts().head()


print(artist_top)
print("Najczęściej występujący artyści na liście")




table.rename(str.capitalize, axis='columns', inplace = True)
table.head()
print(table.head())
print("Tabela po zmianie nazw kolumn")




table.drop(columns = 'Max poz', inplace = True)

table.head()
print(table.head())
print("Tabela po usunięciu kolumny  Max poz")




table_y_max = table['Rok'].value_counts()
table_y_max.head()
print(table_y_max.head())
print("Rok,w którym wydano najwięcej albumów")




t_60_90 = table[(table['Rok'] >= 1960) & (table['Rok'] <= 1990)]['Rok']
t_60_90.count()
print(t_60_90.count())
print("Liczba albumów wydanych w latach 1960-1990")



table[table['Rok'] == max(table['Rok'])]
print(table[table['Rok'] == max(table['Rok'])])
print("Rok,w którym wydano najnowszy album")



artist_first_on_top = table.groupby('Artysta').agg({'Tytuł':'first','Rok':'min'})
artist_first_on_top.sort_values('Rok').head()
print(artist_first_on_top.sort_values('Rok').head())
print("Lista najwcześniej wydanych albumów każdego artysty")







list_to_excel = artist_first_on_top.sort_values('Rok')

list_to_excel.to_csv('ArtistFirstOnTop.csv', index=False)
print(list_to_excel.to_csv('ArtistFirstOnTop.csv', index= False))


print("Zapis do pliku csv zakończony")