"""
Save a list of all the files in the project directory
"""
import os

print("The files and folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)

print("The files and folders in", os.getcwd(), "are:")
items = os.listdir('.')
for item in items:
    print(item)
