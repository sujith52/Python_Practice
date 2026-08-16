class Animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        return "I am an animal "

class Dog(Animal):
    def speak(self):
        return "boww bowwh"

dog1 = Dog("Chintu")
print(dog1.name)
print(dog1.speak())

print("the polymorphism ------")

class Car:
    def start(self):
        return "the car was starting"

class Bike:
    def start(self):
        return "the bike of arjun reddy was starting !"
class Bus:
    def start(self):
        return "the bus was starting !"
def start_transport(transport):
    print(transport.start())

my_car = Car()
my_bike = Bike()
my_bus = Bus()

start_transport(my_car)
start_transport(my_bike)
start_transport(my_bus)

print("the dunder methods - magic methods ")
class Complexnum:
    def __init__(self,real,img):
        self.real =real
        self.img = img
    def __add__(self, other):
        return Complexnum(self.real + other.real , self.img + other.img )
    def __str__(self):
        return f"{self.real}+{self.img}"

c1 = Complexnum(1,2)
c2 = Complexnum(3,4)

c3 = c1 + c2
print(f"the sum of complex num is {c3}")

print("constructor in python !")

class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def display_info(self):
        print(f"the name is {self.name} and salary is {self.salary} , dep: {self.department}")

emp1 = Employee("Sujith",50000,"IT")
emp1.display_info()

print("super() in python --------")

class Animal:
    def __init__(self,name):
        self.name = name 

    def speak(self):
        print(f"the animal {self.name} was making sound !")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"the {self.name} the {self.breed} is making sound !")

dog1 = Dog("Chinmtu","Golden Retriver!")
dog1.speak()
