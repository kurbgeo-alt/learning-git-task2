import sys
import logging
class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename = 'kalkulator.log', level = logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')






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
   
        




def main():
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1- Dodawanie 2 - Odejmowanie, 3 - Mnożenie, 4- Dzielenie")
    logging.debug(f"Użyj działania {operation}")
    if operation in ('1', '2','3', '4'):
         num1= int(input("Podaj pierwszy składnik: 3.0"))
         num2 = int(input("Podaj drugi składnik: 1.7"))


    
    
    if operation == '1':
         print(num1, "+", num2, "=", add(num1,num2))
    elif operation == '2':
         print(num1, "-",num2, "=", substract(num1,num2))
    elif operation == '3':
         print(num1, "*", num2,"=",multiply(num1,num2))
    elif operation == '4':
         print(num1,"/",num2,"=",divide(num1,num2))

    if __name__ == "__main__":
         print(result)     
        