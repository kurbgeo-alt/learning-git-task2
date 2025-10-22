from faker import Faker
def fake_contacts(is_business,amount):
       fake = Faker(locale = 'pl_PL')
       first_name = fake.first_name()
       last_name = fake.last_name()
       phone__number = fake.phone_number()  
       company_position = fake.job()
       company_number = fake.company_number()    
       
       
class BaseContact:
    def __init__(self , first_name, last_name, phone, email):
      self.first_name = first_name
      self.last_name = last_name
      self.phone = phone
      self.email = email
        

    @property
    def label_length(self):
      return len(self.name)
      
    
    
    
    

    def contact(self): 
       print(f'Wybieram numer  {self.phone} i dzwonię do {self.first_name}') 

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, company_position, company_name, company_number):
       super().__init__(name, phone, email)
       self.first_name = first_name
       self.last_name = last_name
       self.phone = phone
       self.email = email
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number

    
    
          
       
    def contact(self): 
       print(f'Wybieram numer służbowy  {self.company_number} i dzwonię do {self.name} z firmy {self.company_name}')

    
    list_of_contacts = []
    for i in range(amount):
        if is_business:
          card = BusinessContact(name, telephone_number, email, company_number, company_position, company_name)
        else:
          card = BaseContact(name, telephone_number, email)
        list_of_contacts.aZppend(card)
        return list_of_contact
                



n = 10

contacts = create_contacts(True,5)
for c in contacts:
  c.contact()


name = "Jan Kowalski"
phone = 123456789
email = "jan34@gmail.com"








