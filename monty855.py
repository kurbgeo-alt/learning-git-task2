import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. WCZYTANIE DANYCH STRZELANIN
# ------------------------------------------------------------
df = pd.read_csv('fatal-police-shootings-data.csv')

df['signs_of_mental_illness'] = df['signs_of_mental_illness'].astype(str).str.lower() == "true"

group = df.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)
group['total'] = group.sum(axis=1)
group['percent_with_mental_illness'] = group[True] / group['total'] * 100

print(group)
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

# ------------------------------------------------------------
# 3. POPULACJA USA – wersja odporna na zmiany Wikipedii
# ------------------------------------------------------------
pop_tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population")

# Najczęściej tabela nr 0 jest główną tabelą
pop = pop_tables[0].copy()

# Normalizacja nazw kolumn
pop.columns = [c.lower() for c in pop.columns]

# Znajdź kolumnę populacji (zmienia się na przestrzeni lat)
pop_col = [c for c in pop.columns if "population" in c][0]

# Kolumna z nazwą stanu/terytorium — zwykle pierwsza
state_col = pop.columns[0]

pop = pop[[state_col, pop_col]].rename(columns={
    state_col: 'state',
    pop_col: 'population'
})

# CZYSZCZENIE POPULACJI
pop['population'] = (
    pop['population']
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.extract(r"(\d+)")
    .astype(float)
)

# Usuwamy terytoria nieposiadające skrótów USPS
pop = pop[~pop['state'].str.contains("District|Puerto|Guam|Samoa|Virgin|Mariana", case=False)]

# ------------------------------------------------------------
# 4. SKRÓTY STANÓW – stabilne pozyskiwanie
# ------------------------------------------------------------
abbr_tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_U.S._state_and_territory_abbreviations")

# Szukamy tabeli, która ma kolumnę USPS
for tbl in abbr_tables:
    cols = [c.lower() for c in tbl.columns]
    if "usps" in cols or "usps abbreviation" in cols:
        abbr = tbl.copy()
        break

abbr.columns = [c.lower() for c in abbr.columns]

# Kolumny: nazwa + skrót
name_col = [c for c in abbr.columns if "state" in c or "name" in c][0]
usps_col = [c for c in abbr.columns if "usps" in c][0]

abbr = abbr[[name_col, usps_col]].rename(columns={
    name_col: "state",
    usps_col: "abbreviation"
})

# Czyszczenie nazw (usuwanie przypisów typu [a])
abbr['state'] = abbr['state'].str.replace(r"\[.*?\]", "", regex=True).str.strip()

# ------------------------------------------------------------
# 5. ŁĄCZENIE
# ------------------------------------------------------------
merged_pop = pop.merge(abbr, on='state', how='left')

# Liczenie incydentów per stan
counts_by_state = df['state'].value_counts().reset_index()
counts_by_state.columns = ['abbreviation', 'incidents']

merged = counts_by_state.merge(merged_pop, on='abbreviation', how='left')

missing = merged[merged['population'].isna()]
if not missing.empty:
    print("\n⚠ Brak dopasowanej populacji dla:")
    print(missing[['abbreviation', 'incidents']])

merged['incidents_per_1000'] = merged['incidents'] / merged['population'] * 1000

print("\nPrzykładowe dane:")
print(merged.head())
