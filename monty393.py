import sys
import logging
logging.basicConfig(filename = 'kalkulator.log', level = logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')
dane_od_użytkownika =input(("Podaj działanie,posługując się odpowiednią liczbą: 1-Dodawanie, 2-Odejmowanie, 3-Mnożenie, 4-Dzielenie:"))
liczba2 = float(input("Podaj składnik: 1. 2.3"))
liczba3 = float(input("Podaj składnik: 2. 5.4"))
logging.info(f"Dodaję {liczba2} i {liczba3}")
wynik = liczba2 + liczba3
print(f"Wynik dodawania: {wynik}")
logging.info(f"Odejmuję {liczba2} i {liczba3}")
wynik = liczba2 - liczba3
print(f"Wynik odejmowania: {wynik}")
logging.info(f"Mnożę {liczba2} i {liczba3}")
wynik = liczba2 * liczba3
print(f"Wynik mnożenia: {wynik}")
logging.info(f"Dzielę {liczba2} i {liczba3}")
wynik = liczba2/liczba3
print(f"Wynik działania: {wynik}")
logging.info(f"Wynik działania to {wynik}")