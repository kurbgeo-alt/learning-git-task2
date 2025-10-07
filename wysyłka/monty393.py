import sys
import logging
logging.basicConfig(filename = 'kalkulator.log', level = logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')
liczba1 = 5.4
liczba2 = 2.3
wynik = 7.7


def dodawanie(a,b):
    return a + b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a * b
def dzielenie(a,b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

   

    
                
   


print("Operacje")
print("1 - Dodawanie")
print("2 -Odejmowanie")
print("3 - Mnożenie")
print("4 - Dzielenie")
wybór = input("Podaj rodzaj operacji: (1/2/3/4):")
liczba1 = input("Podaj pierwszy składnik: 3.0 ")
liczba2 = input("Podaj drugi składnik: 1.7 ")



if wybór == '1':
    

    

    wynik = liczba1 + liczba2
    print(wynik)

    
elif wybór == '2':
    
    
    wynik = liczba1 - liczba2
    print(wynik)
    
elif  wybór == '3':
    
    wynik = liczba1 * liczba2
    print(wynik)

 
elif wybór == '4':
    
    wynik = liczba1 / liczba2
    if (liczba2 != 0):
        print(wynik)
    e
        

    
    
















    


    
    



        

