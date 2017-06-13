#!/usr/bin/env python3

with open("../DATA/mystery","rb") as m:
    chars = m.read()

# Elephants
print(chars[::2].decode())

# Dilbert
print(chars[1::2].decode())
