lista_zakupow=[

    ("roquefort",2.0,12.50),
      ("stilton", 1.0,11.24),
          ("brie",1.0,9.30),
            ("gouda", 1.0, 8.55),
              ("edam",1.0,11.0), 
              ("parmezan",3.5,16.50),
                ("mozarella",1.3,14.0),
                  (" czechosłowacki ser z owczego mleka",2.2,122.32)
                  ]



                  
raport = " "
suma = 0

for produkt,masa,cena in lista_zakupow:
    
    raport +=f"{produkt:35}  {masa: 6.2f} kg  {cena:6.2f} zł/kg/n "
suma += masa * cena
raport += "-" *(35 +6+7+6+6) +"\n"
raport += f"{'suma':{35 +6 +7}} {suma:6.2f} zł"   
print(raport)    
    
    
    






