#!/usr/bin/env python3

# In the command line, make sure you've done a "pip install requests" before running this code!

import requests

customers_response = requests.get('http://nextgeneducation.com/weasley/customers.json')

print(customers_response.status_code)
print(customers_response.headers['content-type'])
print(customers_response.json())

customers = customers_response.json()
print()
print("{0:12s}\t{1:18s}\t{2:25s}".format('First Name', "Last Name", "Email"))

for cust in customers:
    print("{0:12s}\t{1:18s}\t{2:25s}".format(cust['firstName'], cust['lastName'], cust['email']))