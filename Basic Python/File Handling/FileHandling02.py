with open("hello.txt","rt") as f:
    data = f.read()
    print(data)
    f.seek(0)
    for lines in f:
        print(lines.strip())

with open("file_handling.jpg", "rb") as f:
    data = f.read()
    print(data)

import os
file_path = "example.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        print(data)
else:
    print(f"The file {file_path} doestnt exist")

try:
    with open("doestmt.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")
except IOError:
    print("there was an input error occored in there !")
