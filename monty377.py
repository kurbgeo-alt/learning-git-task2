def czy_palindrom(slowo):
    """
    
    sprawdza,czy podane słowo jest palindromem:
    Argumenty:
    slowo(str): Słowo do sprawdzenia
    Zwraca:
    boolean: True,jeśli słowo jest palindromem,w przeciwnym razie False
    """
    slowo ="kajak"
    odwrocone_slowo =slowo[::-1]
    
    if slowo == slowo[::-1]:
        print(czy_palindrom("kajak"))
        return True
    else:
        return False
    
    
        
    