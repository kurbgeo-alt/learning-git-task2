def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba **0.5) +1):
        if liczba % i == 0:
            return False
        return True

oryginalna_lista =[1,2,3,5,6,11,12,18,19,21]
liczby_pierwsze = []
for liczba in oryginalna_lista:
    if czy_pierwsza(liczba):
        liczby_pierwsze.append(liczba)
        print(liczby_pierwsze)


