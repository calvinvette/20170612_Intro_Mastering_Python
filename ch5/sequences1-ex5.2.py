#!/usr/bin/env python3

ctemps = [ -40, 0, 37, 75, 100, -1 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

computer_people = [
    ('Bill', 'Gates', 'Windows'),
    ('Bill', 'Joy', 'Sun Microsystems'),
    ('Brian', 'Kernighan', 'Unix'),
    ('Dennis', 'Ritchie', 'Unix'),
    ('Ken', 'Thompson', 'Unix'),
    ('Guido', 'van Rossum', 'Python'),
    ('Larry', 'Wall', 'Perl'),
    ('Yukihiro','Matsumoto', 'Ruby'),
    ('John', 'Osterhout', 'TCL'),
    ('Linus', 'Torvalds', 'Linux'),
]

for c in ctemps:
    f = ((9 * c) / 5 ) + 32
    print("{0:.1f} C is {1:.1f} F".format(c, f))
print()

