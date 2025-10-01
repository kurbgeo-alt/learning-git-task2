def czy_palindrom(slowo:str) -> bool:

    """
    
    Sprawdza,czy podane słowo jest palindromem:
    Argumenty:
    slowo(str): Słowo do sprawdzenia
    Zwraca:
    bool: True,jeśli słowo jest palindromem,w przeciwnym razie False
    """
    return slowo == slowo[::-1]
print(czy_palindrom("kajak")) # True
print(czy_palindrom("python")) # False
print(czy_palindrom("potop")) # True
print(czy_palindrom("python")) # False
    
    
    
        
    