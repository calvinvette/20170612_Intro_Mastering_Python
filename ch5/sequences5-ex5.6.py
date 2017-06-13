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

for firstname, lastname, thing in computer_people:
    print(lastname.upper())
print()
