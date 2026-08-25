file = open("example.txt","r")
content = file.read()
print(content)
file.close()

file = open("example.txt","r")
content = file.readlines()
print(content)
file.close()

file = open("hello.txt", "w" )
file.write("Hello python this is from sujith ")

file = open("hello.txt","r")
content = file.read()
print(content)

file = open("hello.txt","w")
file.write("destroying the old contents")

file = open("hello.txt","r")
info = file.read()
print(info)
file.close()

f = open("hello.txt", 'a')
f.write("\n the python was bright as a star")

f = open("hello.txt", "x")

with open("hello.txt","r") as f:
    info = f.read()
    print(info)

with open("hello.txt","a") as f:
    f.write("\nSujith is good ")
    f.write("\nHello people of binary torn legasy world?")

students = [
    "sujith\n", "sreejas\n","lathas\n"
]
with open("hello.txt",'a') as f:
    f.writelines(students)

with open("hello.txt",'r') as f:
    for line in f:
        print(line +"       hi      ")

with open("hello.txt",'r' ) as f:
    for line in f:
        print(line.strip())

file = open("hello.txt","r")
print(file.read(21))
print(file.tell())
file.seek(0)
print(file.read(5))
print(file.tell())

try:
    with open("doest.txt","r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"The error {e}")

with open("hello.txt", "a" , encoding="utf-8") as f:
    f.write("నమస్కారం Sujith 😎")
 
with open("hello.txt","r", encoding="utf-8") as f:
    print(f.read())

with open("hello.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)