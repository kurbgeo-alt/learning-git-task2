import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_csv('fatal-police-shootings-data.csv')

df['signs_of_mental_illness'] = df['signs_of_mental_illness'].astype(str).str.lower() == "true"

# Grupowanie wg rasy i chorób psychicznych
group = df.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)
group['total'] = group.sum(axis=1)

# Poprawny odsetek (tylko TRUE)
group['percent_with_mental_illness'] = group[True] / group['total'] * 100

print(group)

# Najwyższy odsetek chorób psychicznych w interwencjach
top_race = group['percent_with_mental_illness'].idxmax()
top_value = group['percent_with_mental_illness'].max()

print("\nRasa z najwyższym odsetkiem przypadków z chorobami psychicznymi:")
print(f"{top_race}: {top_value:.2f}%")

# Dni tygodnia
df['date'] = pd.to_datetime(df['date'])
df['day_of_week'] = df['date'].dt.day_name()

ordered_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
counts_by_day = df['day_of_week'].value_counts().reindex(ordered_days)

plt.figure(figsize=(10,6))
counts_by_day.plot(kind='bar', color='steelblue')

plt.title("Liczba śmiertelnych interwencji policji wg dnia tygodnia")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Liczba interwencji")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()

# --- Pobieranie populacji USA ---
pop_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population')

pop = None
for tbl in pop_tables:
    if any("population" in str(col).lower() for col in tbl.columns):
        pop = tbl
        break

if pop is None:
    raise ValueError("Nie znaleziono tabeli populacji.")

# Normalizacja nazw kolumn
pop.columns = [c.lower() for c in pop.columns]
pop = pop.rename(columns={pop.columns[0]: 'state'})

pop = pop[['state', 'population']]

# Czyszczenie populacji
pop['population'] = (
    pop['population']
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+)")
    .astype(float)
)

# --- Skróty stanów ---
abbr_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations')

abbr = None
for tbl in abbr_tables:
    if 'State/Territory' in tbl.columns and 'Abbreviation' in tbl.columns:
        abbr = tbl[['State/Territory', 'Abbreviation']]
        break

abbr = abbr.rename(columns={'State/Territory': 'state', 'Abbreviation': 'abbreviation'})

# Połączenie tabel
pop = pop.merge(abbr, on='state', how='left')

# Liczenie incydentów per stan
counts_by_state = df['state'].value_counts().reset_index()
counts_by_state.columns = ['abbreviation', 'incidents']

merged = counts_by_state.merge(pop, on='abbreviation', how='left')


missing = merged[merged['population'].isna()]
if not missing.empty:
    print("\n⚠ Brak dopasowanej populacji dla:")
    print(missing[['abbreviation', 'incidents']])
merged['incidents_per_1000'] = merged['incidents'] / merged['population'] * 1000

print("\nPrzykładowe dane:")
print(merged.head())







