# difference btw class and onject

# class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def intoduce(self):
        print(f"the person name is {self.name} and age is {self.age}")

# object
per1 = Person("sujith",22)
per2 = Person("sreejas",22)
per1.intoduce()
per2.intoduce()


class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        print(f"{self.make} {self.model} says honk !")

class Car(Vehicle):
    def __init__(self, make, model, year,color):
        super().__init__(make, model, year)
        self.color = color
    def honk(self):
        print(f"{self.make} , {self.model} with color {self.color} says i am car !")
    def parenthonk(self):
        return super().honk()

car1 = Car("toyata","camry",2020,"black")
car2 = Car("Honda","civic",2019,"blue")
car1.honk()
car2.honk()
car2.parenthonk() #getting the parentclass method using the super ()

# encapsulation 
class Bankaccount:
    def __init__(self,account_number,balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def check_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print(f"some body get this beggers out of this city !")

bank1 = Bankaccount(6304)
print(bank1.check_balance())
bank1.deposit(1000)
bank1.withdraw(2000)
bank1.deposit(200)
print(bank1.check_balance())
print(bank1._Bankaccount__balance)
print(bank1.__dict__)

# acces modifiers 
class Acess:
    def __init__(self,public,protected,private):
        self.public = public
        self._protected = protected
        self.__private = private

ace = Acess("hi","helllo","bye")
print(ace.__dict__)
print(ace.public)
print(ace._protected)
print(ace._Acess__private) #name Mangling !!

