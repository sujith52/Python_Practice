try:
    x = 10 / 2
except ZeroDivisionError as e:
    print(f"the error {e}")
else:
    print(f'well there were no exceptions raied the output is {x} ')

print('creating custom exceptions in teh python ')

class InsufficientFundsErro(Exception):
    """Raised when the bank account dont have the money !"""
    def __init__(self, message = None):
        if message is None:
            message = "Insufficient funds for the transaction !"
        super().__init__(message)
def withdraw(acc_bal,ammount):
    if ammount > acc_bal:
        raise InsufficientFundsErro("Get these beggars out of city !")

acc_bals = 200
# withdraw(acc_bals, 500)

print("using exceptions in the file handling !")

def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError as e:
        print(f"Error : {e}")
        raise
    except IOError as e:
        print(f"Error : {e}")
        raise
    finally:
        print("Cleaning up the resources !")
try:
    data = read_data_from_file("exception.txt")
except FileNotFoundError:
    print("enter a valid file name bro !")

# age = 15
# assert age >= 18, "Age must be above 18"

def cal_age(birth,current):
    age = current - birth
    assert age >= 0, "Age cannot be in negitive bro"
    print(f"yours age is {age}")
try:
    cal_age(2004,2026)
except AssertionError as a:
    print(f"The error is {a}")

try:
    x = 10 / 0
except ArithmeticError as a:
    print(a)

try:
    x = 10 / 0
except ZeroDivisionError as a:
    print(a,"zero divison error has occured !")
    try:
        y = int("invalid_number")
    except ValueError as e:
        print("a value error has occured !",e)

