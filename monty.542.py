from faker import Faker

class BaseContact:
    def __init__(self , name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    
    def label_length(self):
      return len(self.name)
    
    
    
    

    def contact(self): 
       print(f'Wybieram numer +48 {self.phone} i dzwonię do {self.name}') 

class BusinessContact(BaseContact):
    def __init__(self, name, phone, email, company_position, company_name, company_number):
       super().__init__(name, phone, email)
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number

    
    
          
       
    def contact(self): 
       print(f'Wybieram numer służbowy +48 {self.company_number} i dzwonię do {self.name}')

    def fake_contacts(is_business,amount): 
       fake = Faker(['th_TH', 'pl_PL'])
       company_position = fake.job()
       company_name = fake.company()
       email = fake.email()
       name = fake.name()
       telephone_number = fake.number()[3:]
       company_number = fake.number()[3:]
    
    list_of_contacts = []
    for i in range(amount):
        if is_business:
          card = BusinessContact(name, telephone_number, email, company_number, company_position, company_name)
        else:
          card = BaseContact(name, telephone_number, email)
        lista_of_contacts.append(card)

    return lista_of_contacts




n = 10

fake_contacts(True, n) # biznesowe kontakty
fake_contacts(False, n) # normalne kontakty  


name = "Jan Kowalski"
phone = 123456789
email = "jan34@gmail.com"








