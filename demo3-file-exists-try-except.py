#!/usr/bin/env python3

try:
    with open("c:/Users/student/Documents/read.txt.txt", "r") as file1:
        for line in file1:
            print(line[:-1])
except FileNotFoundError as fnfe:
    print("File Doesn't Exist.")



