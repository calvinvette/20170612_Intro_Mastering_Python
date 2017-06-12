#!/usr/bin/env python3

import sys

myName = 'Harry'
description = '''
Harry Potter is the "Boy Who Lived".
He's credited with defeating the dark wizard Voldemort.
He is now an Auror...
'''
print('Hello, World')

print(myName)

print(description)

# Adjacent String literals concatenate
print('foo' 'bar')
# Adjacent String literals don't concatenate with the "."
# print('foo' . 'bar')
# Adjacent String literals concatenate with the "+" sign
print('foo' + 'bar')
# Adjacent String variables don't concatenate
# print(myName description)

print('foo\nbar')

# print('foo
#       bar)

myDir = 'c:\\Program Files\\MySQL\drivers\\'

myDir = r"c:\Program Files\MySQL\drivers\\"

myDirUC = myDir.upper()

print(myDir)
print(myDirUC)

fullScriptPath = sys.argv[0]

print("Script Name:", fullScriptPath)

scriptParts = fullScriptPath.split('/')

print(scriptParts)

lenOfScriptParts = len(scriptParts)
print(lenOfScriptParts)

print(scriptParts[lenOfScriptParts - 1])

print(sys.argv[0].split('/')[-1])

userName = sys.argv[1]
print(userName)

password = input("Enter password: ")

print("Pass: ", password)


# posixifying