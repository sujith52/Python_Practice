print("Comprehensions in python !")

squares = [x ** 2 for x in range(1,8)]
print(f"The squares are {squares}")

sum = [x + x for x in range(1,6)]
print(sum)
sub = [ x for x in range(1,6)]
print(sub)

print("list comprehension")
squa = [x ** x for x in range(1,6)]
print("the list sqaures : ", squa)
print("Dictionary comprehension !")
dicts = {x : x ** x for x in range(1,6)}
print(dicts)
print("Set comprehension")
sets = {char for char in "Sujith Kumar"}
print(sets)

nums = [1,2,3,4,5]
sqaured = [x * x for x in nums]
print(sqaured)
print(f"outs : {[x  for x in nums if x % 2 != 0]}")

origi_list = [1,2,3,4,5,6,7,8,9,10,11,52]
even = [x for x in origi_list if x % 2 ==0 ]
print(even)

fruits = ['apple','guava','pineapple','banana']
sorts_fruits = [fru if fru != "apple" else "apple slice" for fru in fruits]
print(sorts_fruits)

set_nums = [2,3,2,4,5,54,32,2,4,43,2,2,34,3,43,32,2]
unique = {x  for x in set_nums }
print(unique)
print([x ** 2 for x in unique])
print([x + 1 for x in range(1,8) ])


print({num : num * num for num in nums})
print({n: n - 1 for n in nums })

def safe_div(x):
    return x / 2 if x % 2 ==0 else None
nums = [ 1, 2, 3, 4, 5, 6, 7, 8]
print([safe_div(num ) for num in nums])

def squ_fun(x):
    return x * x if x % 2 ==0 else x
print([squ_fun(n) for n in nums])

print([n for n in nums if n % 2 != 0 ])

people = [
    {"name" : "Sujith", "age" : 22, "status": "single"},
    {"name" : "Sreeja", "age" : 22, "status": "single"},
    {"name" : "latha", "age" : 22, "status": "single"},
    {"name" : "preethy", "age" : 30, "status": "married"},
]
invites = [person["name"] for person in people if person["age"] >= 22 and person["status"] == "single"]
print(invites)
overaged = [person["name"] for person in people if person["age"] > 20]
print(overaged)
print([x["name"] +" "+ x["status"] for x in people])

sq_list = [x ** 2 for x in range(10)]
print(sq_list)

empty = []
for x in range(10):
    empty.append(x * 2)
print(empty)

squ_gen = (x ** 2 for x in range(10))
for sq in squ_gen:
    print(sq, end=" ")

import time
start = time.time()
loops = []
for x in range(1, 500):
    loops.append(x * 2 )
print(len(loops))
ends = time.time
