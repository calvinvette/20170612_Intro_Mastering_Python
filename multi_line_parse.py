#!/usr/bin/env python3

# import os
# import sys

lines = []

with open("ml_input.txt") as inp:
    for line in inp:
        line = line.rstrip()
        if line.find('<') > 0:
            parts = line.split("<")
            for part in parts:
                if (part.startswith("<")):
                    lines.append(part)
                else:
                    lines.append("<" + part)
        else:
            lines.append(line)

print(lines)