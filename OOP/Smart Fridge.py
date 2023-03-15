from datetime import date      

class SmartFridge:
    fridge_count = 0

    # přidat food list
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.birth_date = date.today()                  
        SmartFridge.fridge_count += 1
        self.food = []
        
    def greet(self):
        print(f'Hello from {self.brand} {self.model}!')
        
    def tell_age(self):                                 
        td = date.today() - self.birth_date
        print('I am {} days old.'.format(td.days))

    def add_food(self, food):
        self.food.append(food)
        print(f'I have added {food} in my fridge.')

    def remove_food(self, food):
        self.food.remove(food)
        print(f'I have removed {food} from my fridge.')  

    def list_of_food(self):
        print(f"List of food is : {self.food}")

myfridge = SmartFridge('Bosch', 'GSX961NSAZ')


myfridge.greet()
myfridge.tell_age()
myfridge.add_food('milk')
myfridge.add_food('eggs')
myfridge.add_food('cheese')
myfridge.remove_food('milk')
myfridge.list_of_food()
