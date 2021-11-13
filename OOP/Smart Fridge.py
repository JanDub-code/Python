from datetime import date      

class SmartFridge:
    fridge_count = 0
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.birth_date = date.today()                  
        SmartFridge.fridge_count += 1
        
    def greet(self):
        print(f'Hello from {self.brand} {self.model}!')
        
    def tell_age(self):                                 
        td = date.today() - self.birth_date
        print('I am {} days old.'.format(td.days))

myfridge = SmartFridge('Bosch', 'GSX961NSAZ')


print(myfridge.greet())
print(myfridge.tell_age())

