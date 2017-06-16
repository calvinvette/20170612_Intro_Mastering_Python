#!/usr/bin/env python3

import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('customers.xls')

for idx in df.index:
    print("%s %s" % (df['firstName'][idx], df['lastName'][idx]))


custDict = df.to_dict()

print(custDict)