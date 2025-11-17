import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('fatal-police-shootings-data.csv')
df['signs_of_mental_illness'] = df['signs_of_mental_illness'].map({'True': True, 'False': False})
df['signs_of_mental_illness'] = df['signs_of_mental_illness'].fillna(False)


group = df.groupby(['race','signs_of_mental_illness']).size().unstack(fill_value =0)
group['total'] = group.sum(axis=1)
group['percent_with_mental_illness'] =group[True]/group['total']*100


top_race_tuple = group['percent_with_mental_illness'].idxmax()
top_race = top_race_tuple[0]
top_value = group['percent_with_mental_illness'].max()

print("Rasa o najwyższym odsetku chorób psychicznych podczas interwencji:")
print(f"{top_race}: {top_value:.2f}%")


df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()
ordered_days =['Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday']
counts_by_day = df['day_of_week'].value_counts().reindex(ordered_days)
print("Unikalne dni tygodnia w danych:",df['day_of_week'].unique())

plt.figure(figsize=(10,6))
counts_by_day.plot(kind='bar', color='steelblue')

plt.title("Liczba śmiertelnych interwencji policji wg dnia tygodnia")
plt.xlabel("Dzień tygodnia") 
plt.ylabel("Liczba interwencji")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()
pop_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population')

# Wybierz tabelę zawierającą kolumnę z populacją
pop = None
for tbl in pop_tables:
    if any("population" in col.lower() for col in tbl.columns):
        pop = tbl
        break

if pop is None:
    raise ValueError("Nie znaleziono tabeli z populacją na Wikipedii.")

# Znajdź kolumnę populacji
pop_col = [c for c in pop.columns if "population" in c.lower()][0]

# Normalizacja kolumn
pop = pop.rename(columns={pop.columns[0]: 'state', pop_col: 'population'})
pop = pop[['state', 'population']]

# Usuwanie przecinków, konwersja na liczby
pop['population'] = (
    pop['population']
    .astype(str)
    .str.replace(',', '')
    .str.extract(r'(\d+)')  # wyciąga liczby, nawet jeśli są inne znaki
    .astype(float)
)

# --- Pobieranie skrótów stanów (odporne na zmiany tabel) ---
abbr_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations')

abbr = None
for tbl in abbr_tables:
    if 'State/Territory' in tbl.columns and 'Abbreviation' in tbl.columns:
        abbr = tbl
        break

if abbr is None:
    raise ValueError("Nie znaleziono tabeli skrótów stanów.")

abbr = abbr.rename(columns={'State/Territory': 'state', 'Abbreviation': 'abbreviation'})
abbr = abbr[['state', 'abbreviation']]


pop = pop.merge(abbr, on='state', how='left')


counts_by_state = df['state'].value_counts().reset_index()
counts_by_state.columns = ['abbreviation', 'incidents']

merged = counts_by_state.merge(pop, on='abbreviation', how='left')


missing = merged[merged['population'].isna()]
if not missing.empty:
    print("\n⚠ Uwaga! Nie udało się dopasować populacji dla:")
    print(missing[['abbreviation', 'incidents']])


merged['population'] = merged['population'].astype(float)


merged['incidents_per_1000'] = merged['incidents'] / merged['population'] * 1000

print("\nPrzykładowe dane:")
print(merged.head())







