#!/usr/bin/env python

done = False

while not done:
	c = input('Enter Celsius temp: ')
	if c.lower() == 'q':
		done = True
	# if c[0].isalpha():
	else:
		c = float(c)
		f = ((9 * c) / 5 ) + 32
		print('{0:.1f} C is {1:.1f} F\n'.format(c,f))


print('Thanks for using our program!')