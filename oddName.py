"""
Lindsay Ward
"""

name = input("Name: ")
while name == "":
    print("Name can not be blank")
    name = input("Name: ")
for i in range(0, len(name), 2):
    print(name[i])

