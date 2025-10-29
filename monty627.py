import pandas as pd

df = pd.DataFrame('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/')
albumy_wszechczasow = {
    'Tytuł':{'1':'THE GREATEST HITS','2':'GOLDEN HITS ', '3':'SQT.LONELY HEARTS CLUB BAND', '4':'21', '5': 'WHAT\'S THE STORY MORNING GLORY'},
    'Artysta':{'1':'Queen', '2': 'ABBA', '3': 'The Beatles', '4': 'Adele', '5': 'Oasis'},
    'Rok wydania':{'1':1981, '2':1976, '3':1967, '4':2011, '5':1995},
    'Max pozycja w UK' :{'1':1, '2':1, '3':1, '4':1,'5':2}
    

}
def wyszukaj_po_artyście(artysta):
    wyniki = []
    for album in albumy_wszechczasow:
        if album['artysta'].lower() == artysta.lower(): 
             wyniki.append(album)
    return wyniki         


znalezione_albumy = wyszukaj_po_artyście('Adele')
print(znalezione_albumy)

df.sort_values(by='Rok wydania', ascending = False,inplace =True)
print(df)
