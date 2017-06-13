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

clean_fruits =  [ f.strip().lower() for f in fruits ]

print(','.join(clean_fruits))
print()

# Equivalent to "join" phrasing above:
cf_count = len(clean_fruits)
for (idx, cf) in enumerate(clean_fruits):
    if idx < (cf_count - 1):
        print(cf + ",", end="")
    else:
        print(cf)
