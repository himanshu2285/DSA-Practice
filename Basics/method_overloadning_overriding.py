
# Method Overloading using Default Arguments and *args
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a*b
        for num in args:
            result *= num
        return result
    
obj = Calculator()
print(obj.multiply(2, 3))          # Output: 6
print(obj.multiply(2, 3, 4))       # Output: 24

print(obj.multiply())
print(obj.multiply(5))



# Method Overriding
class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

objs = [Animal(), Dog(), Cat()]
for obj in objs:
    print(obj.sound())
    
    


# Built In Polymorphism Example
print(len("Himanshu"))
print(len([1, 2, 3, 4, 5]))

print(max(10, 20))
print(max(["a","f","d"]))