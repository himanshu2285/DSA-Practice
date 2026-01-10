
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


# Super Keyword Example
class Parent:
    def __init__(self, surname):
        self.surname = surname
    
    def info(self):
        return f"Parent Surname: {self.surname}"

class Child(Parent):
    def __init__(self, name, surname):
        super().__init__(surname)
        self.name = name
        
    def info(self):
        print(super().info())
        return f"Child Name: {self.name}, Surname: {self.surname}"


child = Child("Alice", "Smith")
print(child.info())



