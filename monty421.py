import sys
import logging
logging.basicConfig(level=logging.INFO)






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
   
operations = {
    "1":("Dodawanie",add,"+"),
    "2":("Odejmowanie",substract,"-"),
    "3":("Mnożenie",multiply,"*"),
    "4":("Dzielenie",divide,"/"),
}

def main():
     while True:
          print("/Podaj działanie:")
          for key, (name, _,symbol) in operations.items():
               print(f"{key} - {name} ({symbol})")
          op = input("Wybór(lub 'q' aby wyjść):").strip()
          if op == "q":
               print("Do widzenia")
               break
          if op not in operations:
               print("Niepoprawny wybór.")
               continue
          try:
               a=float(input("Podaj pierwszą liczbę:"))
               b=float(input("Podaj drugą liczbę:"))
               name,func,symbol = operations[op]
               result= func(a,b)
               print(f"{a} {symbol} {b} ={result}")
          except ValueError as e:
               print(f"Błąd {e}")
if __name__ == "__main__":
          main()                   
          
              
                    
     
               
