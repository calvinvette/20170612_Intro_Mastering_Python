#!/usr/bin/env python3
import sys

# c:\py3workspace\ch3\c2f.py 212
# just a numeric value, no scale - look to the name of the program
if (len(sys.argv) == 2):
    orig_temp_to_convert = sys.argv[1]
    orig_scale = sys.argv[0].split("/")[-1]
elif (len(sys.argv) > 2):
    orig_scale = sys.argv[2]
    orig_temp_to_convert = sys.argv[1]
else:
    orig_scale = input("What temperature scale is the original value in?")
    orig_temp_to_convert = input("What temperature do you want me to convert?")

temp_to_convert = float(orig_temp_to_convert)

c2f = orig_scale.lower().startswith('c')

if (c2f):
    print("C2F:", end=" ")
    result = ((temp_to_convert * 9 / 5)) + 32
else:
    print("F2C:", end=" ")
    result = ((temp_to_convert - 32) / 9) * 5

print("{0:3.2f} = {1:3.2f}".format(temp_to_convert, result))