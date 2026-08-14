print('the methods in python !')

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5
        print(f"the {self.model} is going in a {self.speed} km/h")

    def brake(self):
        self.speed -= 5
        print(f"the {self.model} is going now at speed of {self.speed} km /h")

my_car = Car("Toyata","corolla",2020)
my_car.accelerate()
my_car.brake()

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"the name is {self.name} and age is {self.age}")

std1 = Student("sujith",22)
std2 = Student("sreejas",22)
std3 = Student("lathas",22)
std1.show()
std2.show()
std3.show()

# diff btw fun and method

def add_nums(a,b):
    return a+b

res = add_nums(2,3)
print(f"the result is {res}")

#method
class circle:
    def __init__(self, radius):
        self.radius = radius

    def showRad(self):
        return 3.14 * self.radius * self.radius

cir1 = circle(4)
print(cir1.showRad())

# method overloading 

class pastha:
    def prepare(self, sauce="marina", additional_ing= None):
        if additional_ing:
            print(f"the pastha was made with {sauce} and {additional_ing}")
        else:
            print(f"the {sauce} sauce is used !")

pas = pastha()
pas.prepare()
pas.prepare("chilly sauce")
pas.prepare("chicken", "chinese noodles")

class pappu:
    def make_pappu(self,dal="chenigipappu", green_leaf = None):
        if green_leaf:
            print(f"the pappu was made with {dal} and {green_leaf}")
        else:
            print(f"the papu was made with {dal} dal !")
pa = pappu()
pa.make_pappu()
pa.make_pappu("alasandalu")
pa.make_pappu("kandipappu","ground nuts ")

# method overiding !

class Vechil :
    def start_engine(self):
        print("the overall vechile engine was strating ")

class Car(Vechil):
    def start_engine(self):
        print("the car engine was starting !")

class Bike(Vechil):
    def start_engine(self):
        print("the bike engine was starting bro !")

vech = Vechil()
car = Car()
bik = Bike()

vech.start_engine()
car.start_engine()
bik.start_engine()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def user_info(self):
        name = self.get_name()
        salarys = self.get_salary()
        print(f"the name is {name} and the salary {salarys}")

emp1 = Employee("sujith",20000)
emp2 = Employee("sreejas",50000)
emp1.user_info()
emp2.user_info()

# static method in python 
class Calc:
    @staticmethod
    def add(a,b):
        print(a + b)
    @staticmethod
    def sub(a,b):
        print(a - b)

Calc.add(10,10)
Calc.sub(20,5)

class Students:
    count = 0

    def __init__(self,name):
        self.name = name
        Students.count += 1

    @classmethod
    def student_count(cls):
        return cls.count

stds1 = Students("sujith")
stds2 = Students("sreejas")
stds3 = Students("lathas")
print(Students.student_count())

class Train:
    def __init__(self,make,model,fuel):
        self.make = make 
        self.model = model 
        self.fuel = fuel 

    def drived(self,distance):
        self.fuel -= distance * 0.1
        print(f"the {self.make} and the model {self.model} has fuel {self.fuel}")

tr1 = Train("indian railways","Chennai express",60)
tr1.drived(100)

# method chaining 

class Clci:
    def __init__(self,value = 0):
        self.value = value
    def add(self,num):
        self.value += num
        return self
    def sub(self,num):
        self.value -= num
        return self
    def mul(self,num):
        self.value *= num
        return self
    def result(self):
        return self.value

var1 = Clci()
finals = var1.add(5).sub(1).mul(2).result()
print(f"the final result will be in this format ! {finals}")