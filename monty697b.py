import pandas as pd
df = pd.read_csv('tmbd_movies(1).csv')
df = pd.read_csv('tmbd_genres(1).csv')
df = pd.DataFrame({'vote_average': movie_votes})
table = DataFrame(df)
movie_votes = df('vote_averange').tolist()
for i in range(len(movie_votes)):
    movie_votes[i] = float(movie_votes[i])
    number__of_votes = len(movie_votes)
    total_of_votes = sum(votes.values())
    average_of_votes = total_of_votes/number__of_votes
    print(average_of_votes)
    vote_count ={}
    for vote in movie_votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
            print(vote_count)
            movie_vote = list(vote_count.keys)
            filtered_votes =[]
            sorted_votes = sorted(vote_count.values(), reverse = True)
            for  count in sorted_votes:
                for vote in vote_count:
                    if vote_count[vote] == count and vote not in filtered_votes:
                        filtered_votes.append(vote)
                        print(filtered_votes)
 t_2010_2016 = table[(table['Rok'] >= 2010) & (table['Rok'] <2016)]['Rok']
t_2010_2016.count()
print(t_2010_2016.count())
print("Liczba filmów wydanych w latach 2010-2016: ", t_2010_2016.count())

fig, ax = plt.subplots()

years = np.array(['2010','2011','2012','2013', '2014', '2015', '2016'])
revenues = []

ax.bar(years, revenues)
genre_revenue = table.grouphy('Gatunek')['Przychód'].sum().reset_index()
import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots()
genres = genre_revenue['Gatunek']
revenues = genre_revenue['Przychód']
ax.bar(genres,revenues)
table.runtime{czas trwania filmu w minutach}
short_movies = tabless[table['Czas trwania'] < 60]
long_movies = tables[tables['Czas trwania'] >= 60]
print("Liczba filmów trwających dłużej niż 60 minut: ", long_movies.shape[0])
genre_top10 = table.grouphy('Gatunek') ['Ocena'}.mean().resert(index()).sort.values(by='Ocena', ascending = False().head(10)])
genre_top10.plot(x = 'Gatunek' y ='Ocena', kind = 'barh', legend = False())
print(genre_top10)


                                                                                    



                     
