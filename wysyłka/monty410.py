class  BaseContact:
    

    
    


        
    def __init__(self , name , phone , email):
        self.name = name
        self.phone = phone
        self.email = email
        def label_lenght(self):
            return len(self.name)
    def contact(self):
        print(f'Wybieram numer +48 {self.name} i dzwonię do {self.phone}')


        
        
        


           
            
class BusinessContact(BaseContact):
        def __init__(self, company_position, company_name, company_number):
                     super().__init__(name)
                     
                     self.company_position =company_position
                     self.company_name = company_name
                     self.company_number = company_number
 
                   
name ="Jan Kowalski"
phone = 123456789
