print('multiple inheritance in python ------------')

class ChefChinese:
    def make_noodles(self):
        print("Making a chinese style noodles")
class ChefIndian:
    def make_biryani(self):
        print("making a indian andhra style biryani !")

class ChefStudent(ChefChinese, ChefIndian):
    pass

stud = ChefStudent()
stud.make_noodles()
stud.make_biryani()

print('abstract class and methods -------')

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "Meowww!"

class Dog(Animal):
    def speak(self):
        return "bow boww"
cats = Cat()
dogs = Dog()
print(cats.speak())
print(dogs.speak())

# animals = Animal()

print('static variables ---------')
class Cars:
    wheels = 4  #static variable 
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def show(self):
        print(f"the car maker {self.make} and model {self.model} and wheels {self.wheels}")
nano_cars = Cars("BMW","Balck sfit")
nano_cars.show()
print(nano_cars.wheels)

print('decorators --------')
def my_decorator(func):
    def wrapper():
        print("some security was checked before the exe of func")
        func()
        print('Something is happened after the function ')
    return wrapper

@my_decorator
def say_hello():
    print("my name is sujith")

say_hello()

print('instance, class, static methods ----------')
class Bike:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
bik = Bike("Red")
print(bik.get_color())

# class
class Bike2:
    total_bikes = 0
    def __init__(self):
        Bike2.total_bikes += 1

    @classmethod
    def get_total_bikes(cls):
        return cls.total_bikes
b1 = Bike2()
b2 = Bike2()
b3 = Bike2()
print(Bike2.get_total_bikes())

# static 
class Bike3:
    @staticmethod
    def check_speed(speed):
        return 0 <= speed <= 200

print(Bike3.check_speed(50))

print("well hope you had a good day ahead !")