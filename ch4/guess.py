#!/usr/bin/env python

max_val = 26
min_val = 0
tries = 0

while True:
    guess = int((max_val + min_val)/2)
    ans = input("Is {0} your number? ".format(guess))

    if ans == "q":
        break

    if ans == "h":
        max_val = guess
        tries = tries + 1
    elif ans == "l":
        min_val = guess
        tries = tries + 1
    elif ans == "y":
        tries = tries + 1
        print("I got it in {0} try(ies)!".format(tries))
        break
    else:
        print('''
Please enter h, l, or y
h - if the value is too high
l - if the value is too low
y - if I guessed the right value.
''')

