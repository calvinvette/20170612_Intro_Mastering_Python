#!/usr/bin/env python3

import os.path
import os

file_name = "c:/Users/student/Documents/read.txt"
if os.path.isfile(file_name):
    with open(file_name, "r") as file1:
        for line in file1:
            print(line[:-1])
else:
    print("File Doesn't Exist.")

# os.getcwd() checks the current process directory
directory = os.getcwd()
# directory = "c:/Users/student/Documents/"

# res should either be an empty array or an array with one item in it, "read.txt", if it exists as a file in the directory
res = [entry.name for entry in os.scandir(directory) if entry.is_file() and entry.name == "read.txt"]

print(res)