import sys
import logging






def add(a,b):
    logging.debug(f"Adding {a} + {b}")
    result = a + b
    logging.info(f"Adding result: {result}")
    return result
    
def substract(a,b):
    logging.debug(f"Substracting {a} - {b}")
    result = a -b
    logging.info(f"Substracting result: {result}")
    return result
    
def multiply(a,b):
    logging.debug(f"Multipling {a} * {b}")
    result = a * b
    logging.info(f"Multipling result: {result}")
    return result



    
def divide(a,b):
        if b ==0:
             logging.error("Nie dzieli się przez zero!")
             raise ZeroDivisionError("Division by zero is not allowed.")
        else:
             logging.debug(f"Dividing {a} / {b}")
             result = a/b
             logging.info(f"Division result: {result}")
             return result
   
operation = (
     "1:add"
     "2:substrate"
     "3:multiply"
     "4:divide"
)

symbols = (
     1-"+"
     2 - "-" 
     3 - "*"
     4- "/"
)



def main():
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1- Dodawanie 2 - Odejmowanie, 3 - Mnożenie, 4- Dzielenie")
    logging.debug(f"Użyj działania {operation}")
    
     num1= int(input("Podaj pierwszy składnik:"))
         num2 = int(input("Podaj drugi składnik: "))
    result=operation(operation(num1,num2))    


    
    
    print(f"")

    if __name__ == "__main__":
         main()     
        