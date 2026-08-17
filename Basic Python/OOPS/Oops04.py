print('MRO method Resolution Order ')
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(D.mro())

print("data encapsulation -------")
class Bank:
    def __init__(self):
        self.__balance = 0
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Some body get these beggars out of the city !")
    def show_bal(self):
        print(f"the balance was {self.__balance}")
ban = Bank()
ban.deposit(1000)
ban.withdraw(500)
ban.show_bal()
ban.withdraw(5000)

print("@property calingit like a variable")
class Circle:
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return  self._radius
    @property
    def diameter(self):
        return self._radius ** 2
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
cir1 = Circle(5)
print(cir1.diameter)
print(cir1.radius)
print(cir1.area)

print("Singleton in the python ! same instance only one used again and again ")
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
sing1 = Singleton()
sing2 = Singleton()
print(sing1 is sing2)

def upper_dec(function):
    def wrapper():
        func = function()
        upper_main = func.upper()
        return upper_main
    return wrapper
@upper_dec
def greet():
    return "Hello world !"

print(greet())

print("multiple dispatch")

from functools import singledispatch

@singledispatch
def describe(arg):
    print("this is the generic object",arg)
@describe.register
def _(name:str):
    print(f"Your name is {name}")
@describe.register(int)
def _(args):
    print(f"your is {args} old!")
@describe.register(list)
def _(args):
    print(f"this is the list {args}")

describe("sujith")
describe(22)
describe([1,2,3,4,56])

print("the attributes in py -----------")

class Person:
    def __init__(self):
        self.name = "Sujith"
    def __getattribute__(self, name):
        print(f"some one is acessing the name {name}")
        return super().__getattribute__(name)
per1 = Person()
print(per1.name)

class CustomAttr:
    def __getattr__(self, name):
        print(f"Acessing the attribute {name}")
        return super().__getattr__(name)
    def __setattr__(self, name, value):
        print(f"Setting the attribute {name} : {value}")
        return super().__setattr__(name,value)
    def __delattr__(self, name):
        print(f"Deleting the {name} attribute")
        return super().__delattr__(name)

obj = CustomAttr()
obj.name = "Sujith"
print(obj.name)
del obj.name

