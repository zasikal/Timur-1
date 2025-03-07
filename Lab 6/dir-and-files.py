import os
import string
#2
path = input()
if os.path.exists(path):
    print("The file exists", '\n')
    if os.access(path, os.X_OK):
        print("Executable", '\n')
    else:
        print("Not executable", '\n')
    if os.access(path, os.R_OK):
        print("Readable", '\n')
    else:
        print("Not readable", '\n')
    if os.access(path, os.X_OK):
        print("Writable", '\n')
    else:
        print("Not writable", '\n')
else:
    print("The file doesn't exist", '\n')

#3
path = input()
if os.path.exists(path):
    print("The file exists", '\n')
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("The file doesn't exist", '\n')
#4
path = input()
with open(path, 'r') as file:
    lines = len(file.readlines())
    print(lines)
#5
path = input()
mylist = ['Ginger', 'Latin', 'Asian']
with open(path, 'w') as file:
    file.write(' ,'.join(mylist))
#6
for letter in string.ascii.uppercase:
    f = open({letter}.txt, "x")
#7
path = input()
destination = input()
with open(path, "r") as p, open(destination, "w") as d:
    d.write(p.read())
#8
path = input()
if os.path.exists(path):
    os.remove(path)
    print("The file was deleted")
else:
    print("There is no such file")

