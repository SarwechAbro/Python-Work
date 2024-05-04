class Car:
    def __init__(self, name=None, model=None):
        self.name = name
        self.model = model
    
    def __str__(self):
        return f"{self.name} is by model {self.model}"
    
    def get(self):
        self.name = input("Enter Name: ")
        self.model = input("Enter Model: ")
    

car = Car()
car.get()
print(car.name)