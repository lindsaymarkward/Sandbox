"""
Lindsay Ward
"""


def main():
    name = get_name()
    number = int(input("Print every nth character. n="))
    print_characters(name, number)


def print_characters(string, number):
    for i in range(0, len(string), number):
        print(string[i])


def get_name():
    name = input("Name: ")
    while name == "":
        print("Name can not be blank")
        name = input("Name: ")
    return name


main()
