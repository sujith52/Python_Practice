# the control constructs in python !

weather = "sunny"

if weather == "sunny":
    activity = "Go for a walk !"
elif weather == "rainy":
    activity = "Drink a chai in house !"
else:
    activity = "watch Game of thrones"

print(activity)

# loops
nums = [1,2,3,4,5,6,7,8,9,10]
for i in nums:
    print(f"the number {i} divided by 2 will give result : {i * 2}")

timer = 0
limit = 6

while timer < limit:
    print(f"time passed {timer} in seconds !")
    timer += 1

for i in range(5):
    print(i)

dicts = {"Sujith":"5A4", "sreejas":"599","lathas":"598"}
for student,roll in dicts.items():
    print(f"the name is {student} and roll number is {roll}")

traffic_light = "yellow"

if traffic_light == "green":
    print("boss you can go !")
elif traffic_light == "yellow":
    print("slow down tammudu")
else:
    print("Stop bro !")


marks = 50
# marks = int(input("enter marks bro :"))
if marks >= 90:
    print("A Grade")
if marks >= 80:
    print("B Grade")
if marks >= 70:
    print("C Grade")
if marks >= 60:
    print("D Grade")
else:
    print("F Grade !")


for i in range(2):
    print(i)
print('-----------')
for i in range(2,5):
    print(i)
print('-----------')
for i in range(2,12,2 ):
    print(i)

#  nested loops 

for i in range(1,4):
    for j in range(1,6):
        print(f"{i} X {j} = {i * j}")
    print("--------------")

for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

list_nums = [1,2,3,4,5]
target = 6

for i in list_nums:
    if i == target:
        print(f"i has found the target {i} num")
        break
else:
    print(f"The {target} you are searching was not found in list !")

list_fruits = ["apple","pineapple","custard apple","white aool apple"]
for fruit in list_fruits:
    print(f"the fruit id : {fruit}")

fruits_dict = {"apples":5, "pineapples": 10, "cherries":8}
for [fuit,nums] in fruits_dict.items():
    print(f"the fruit is {fuit} : {nums}")

# pass in loops
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)