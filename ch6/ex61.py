#!/usr/bin/env python3
import sys


arg_count = len(sys.argv) - 1

file_names = []
for filec in range(1, arg_count + 1):
    file_names.append(sys.argv[filec])

print(file_names)

# file_names = [ file_name for filec in range(1, arg_count + 1) file_name]
line_no = 0

for file_name in file_names:
    with open(file_name) as file:
        for line in file:
            line_no += 1
            print("{0}:\t{1}".format(line_no, line[:-1]))
    line_no = 0
