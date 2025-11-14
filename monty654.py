import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Wczytywanie danych
df = pd.read_csv('fatal-police-shootings-data.csv')
#Zestawienie liczby ofiar według rasy i oznak choroby psychicznej
df['signs_of_mental_illness'] = df['signs_of_mental_illness'].astype(bool)


group = df.groupby(['race','sign_of_mental_illness']).size().unstack(fill_value =0)
group['total'] = group.sum(axis=1)
group['percent_with_mental_ilnesses'] =group[True]/group['total']*100

top_race = group['percent_with_mental_illness'].idxmax()
top_value = group['percent_with_mental_illness'].max()

print("Rasa o najwyższym odsetku chorób psychicznych podczas interwencji:")
print(f"{top_race}: {top_value:.2f}%")


df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()
ordered_days =['Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
counts_by_day = df['day_of_week'].value_counts().reindex(ordered_days)
print(df['day_of_week'].unique())

plt.figure(figsize=(10,6))
counts_by_day.plot(kind='bar', color='steelblue')

plt.title("Liczba śmiertelnych interwencji policji wg dnia tygodnia")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba interwencji")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()


pop = pd.read_csv('state_population.csv')  # kolumny np. state, population
abbr = pd.read_csv('state_abbreviations.csv')  # kolumny np. state, abbreviation

# Połączenie  baz danych
pop = pop.merge(abbr, on='state', how='left')

# Zliczenie interwencji wg stanu (zakładam kolumnę state_abbr lub podobną w df)
counts_by_state = df['state'].value_counts().reset_index()
counts_by_state.columns = ['abbreviation', 'incidents']


merged = counts_by_state.merge(pop, left_on='abbreviation', right_on='abbreviation', how='left')


merged['incidents_per_1000'] = merged['incidents'] / merged['population'] * 1000

print(merged.sort_values('incidents_per_1000', ascending=False))

top_states = merged.sort_values('incidents_per_1000', ascending=False).head(10)
print(top_states)






