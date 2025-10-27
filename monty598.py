from faker import Faker
fake = Faker(locale = 'pl_PL')

       
class BaseContact:
    def __init__(self , first_name, last_name, phone, email):
      self.first_name = first_name
      self.last_name = last_name
      self.phone = phone
      self.email = email
        

    @property
    def label_length(self):
      return len(self.first_name) + len(self.last_name) + 1
    
    def contact(self):
       print(f'Wybieram numer  {self.phone} i dzwonię do {self.first_name}') 
    @property
    def full_name(self):
       return f'{self.first_name} {self.last_name}'
       
class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, phone, email, company_position, company_name, company_number):
       super().__init__(first_name,last_name, phone, email)
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number

    def contact(self): 
       print(f'Wybieram numer służbowy  {self.company_number} i dzwonię do {self.full_name} z firmy {self.company_name}')

def create_contacts(is_business, amount):
       list_of_contacts = []
       for i in range(amount):
          if is_business: 
             card = BusinessContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                phone = fake.phone_number(),
                company_position = fake.job(),
                company_name = fake.company(),
                company_number = fake.phone_number()
             )
          else:
             card = BaseContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                email = fake.email(),
                phone = fake.phone_number(),
             )
             list_of_contacts.append(card)
       return list_of_contacts      



             

              

contacts = create_contacts(True,5)
for c in contacts:
 c.contact()
  


             
             
             
       
       


