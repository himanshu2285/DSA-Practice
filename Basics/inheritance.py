
# Single Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        return f"Animal Name: {self.name}"
    
class Dog(Animal):
    def bark(self):
        return "Woof!"
    
dog = Dog("Buddy")
print(dog.info())
print(dog.bark())