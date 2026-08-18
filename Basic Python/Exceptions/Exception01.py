print('Exception handling in python !')

try:
    num = int("not_a_number")
except ValueError as e:
    print(f"Encounteried an exception {e}")

def divide(a,b):
    try:
        result =  a/b
    except ZeroDivisionError:
        print("Error cannot be divided by zero !")
        return None
    return result
res1 = divide(10,5)
print(res1)
res2 = divide(10,0)
print(res2)

try:
    x = 1/0
except ZeroDivisionError:
    print("value cannot be divided by zero !")
except Exception:
    print("An unknown error was appeared !")
finally:
    print("this line will be always executed !")

try:
    # num1 = int(input("Enter the num1 :"))
    # num2 = int(input("Enter the num2 :"))
    num1 , num2 = 2,3
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("Error cant be divided by the zero !")
except ValueError:
    print("Please enter a valid number !")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative bro !")
    else:
        print("Valid age entered !")
try:
    check_age(6)
except ValueError as e:
    print(f"An error occured {e}")


def level3():
    return 1 /0
def level2():
    return level3()
def level1():
    try:
        return level2()
    except ZeroDivisionError:
        print("caught zero division error in level1")
result = level1()

try:
    # x = 1/0
    my_list = [1,2,3]
    print(my_list[3])
except (ZeroDivisionError, IndexError) as e:
    print(f"the error was {e}")

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("cannot divided by zero.") from e
try:
    divide(10,0)
except ValueError as e2:
    print(f"caught an exception : {e2}")
    print(f"Original exception {e2.__cause__}")

print("nested exceptions in the python ---------")
try:
    print('starting of the outer block !')
    try:
        print('the starting of the inner block !')
        result = 1 / 0
    except ZeroDivisionError:
        print(f"the error in the inner block as zero error exception")
    print("end of the outer block !")
except Exception as eo:
    print(f"the error in the our block is {eo}")
    print('this only occurs when the other exception that may occur unexpectedly !')

try:
    x = 1/0
except ZeroDivisionError as e:
    print(f"Error {e}")
finally:
    print(f"the finally block that executes ")

    