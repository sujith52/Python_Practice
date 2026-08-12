a = 10
b = 10.0
c = "10"
d = True

print(a + b)    
print(type(a + b)) 

print(a == b) 
print(a == c)  

print(int(c) + a)
print(str(a) + c)

print(int("25"))
print(float("25"))
print(str(25))
print(int(25.9))
print(int("25"))
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("False"))

Q2Answers = '''
25
25.0
"25"
25
25
false
true
false
True
'''
values = [
    10,
    10.5,
    "hello",
    True,
    3 + 4j,
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"name": "Sujith"}
]
for i in values:
    print(f"{i} is {type(i)}")

# q4
my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

my_list[0] = 100 #true 
# my_tuple[0] = 100 #false , bcz tupple is unmutablle

# q5

names = ["Sujith", "Sreejas"]
names.append("Lathas")
print(names)
names = names.append("Mahesh") #append method modifies and gives the none as result !
print(names)

#q6
students = {
    "Sujith": 65,
    "Sreejas": 92,
    "Lathas": 78,
    "Rahul": 91
}

higest = max(students.values())
low = min(students.values())
avg = sum(students.values()) / len(students)
higeststud = max(students, key=students.get)
nostuds = sum(1 for i in students.values() if i > 80)

print(f"the higest {higest} and lowest : {low} and average {avg} and higest student is {higeststud} and no of students is abve 80 is :{nostuds}")

# Q7
python_students = {"Sujith", "Rahul", "Kiran", "Arun"}
java_students = {"Rahul", "Arun", "Mahesh", "Sreejas"}
print(python_students.intersection(java_students))
print(python_students.difference(java_students))
print(java_students.difference(python_students))
print(python_students.union(java_students))

# Q8

a = 10
b = 3

print(a / b) #3.33
print(a // b) # 3
print(a % b) #1
print(a ** b) #1000

print(a > b and b > 0) #t
print(a < b or b == 3) #T
print(not a == 10) #fase
print("-----------")
#Q9
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) #T
print(a is b) #F

print(a == c) #T
print(a is c) #T

#Q10
q10a = 12
q10b = 3

print(q10a & q10b)
print(q10a | q10b)
print(q10a ^ q10b)
print(q10a <<q10b)
print(q10a >>q10b)

#Q11
marks = 99
if marks >= 90:
    print("A grade ")
elif marks >= 80:
    print("B Grade")
elif  marks >= 70:
    print("C Grade")
else:
    print("D grade !")

#Q12
tr1 = 10
tr2 = 10
tr3 = 5

if (tr1 + tr2 > tr3) or (tr2 + tr3 > tr1) or (tr1 + tr3 > tr1):
    if tr1 == tr2 == tr3:
        print("Equilateral")
    elif tr1 == tr2 or tr2 == tr3 or tr3 == tr1:
        print("isosceles")
    else: 
        print("scalene")
else:
    print("invalid triangle")

#q13 login system !
# user = input("Enter the username : ")
# passw = input("Enter the password : ")
user = "sujith"
passw = "python123"
username = "sujith"
password = "python123"
if user == username and passw == password:
    print("the login was sucessful")
elif user != username:
    print("invalid username ")
elif passw != password:
    print("invalid password")
else: 
    print("invalid username and the password")


