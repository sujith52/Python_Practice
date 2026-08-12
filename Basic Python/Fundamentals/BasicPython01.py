# python basics 
print('hello world !')

name = "Sujith Kumar"
age = 22
print("Hello, my name is ",name,"and my age is ",age,"years old !")

names = ['sujith','sreejas','lathas']
for name in names:
    print("the name is ",name) 

number_of_apples = 15
print(number_of_apples)
print(type(number_of_apples))

weight = 2.5
print(type(weight))

message = "Hello sreejas !"
print(type(message))

is_in_love = False
print(type(is_in_love))

sets = {"599","5A4","5**"}
print(type(sets))

complex_number = 3 + 4j
print(type(complex_number))

lists = ["mahesh babu", "balaya babu", "kalyan babu"]
print(type(lists))

tuples = ("sujith", "kumar")
print(type(tuples))

phone_dict = {"sujith": "6304", "sreejas ": "6305"}
print(type(phone_dict))

# type casting in python

numInt = 101
numFloat = 101.101
addedSum = numInt + numFloat
print(addedSum)
print(type(addedSum))

numInt1 = 123
numString = "123"
Stringnum = int(numString)
sumIs = numInt1+ Stringnum
print(sumIs)
print(type(sumIs))

my_list = [1,2,3,4,5,6]
my_tupple = (1,2,3,4,5,6)

my_list[0] = 123456
print(my_list)

try:
    my_tupple[0] = 1011
except TypeError as err:
    print("the error is : ",err)

mylists = ['hi','bye']
my_list.append('hello')
print(mylists)

greeting = "how are you in life !"
named = greeting + "sreejas ."
print(named)

# arthmetic operators !

a = 10
b = 5

print(a+b , a-b, a*b , a/b)
# comparison operators 
print(a == b, a!= b, a > b, a < b, a>=b, a<=b)
# logical operators 
print(a and b, a or b, not a)
# assigment operators 
num1 = 10
num2 = num1 + 10 # num2 += 10 
print(num2)

# bitwise
print( a & b , a | b, a ^ b, a<<b, a>>b)
# membership operators : in , not in
print(1 in my_list)
print(4 not in my_list)

# identy oprr is, is not 
id1 = [1,2,3]
id2 = id1
id3 = [1,2,3]
print(id1 is id2)
print(id1 is not id3)

