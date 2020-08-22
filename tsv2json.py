# Import lib

import csv
import json
import collections

# aliases
OrderedDict = collections.OrderedDict

src = '/tmp/data.log'
dst = '/tmp/data.json'

# data input output

data=[{}]
with open('data.json', 'w') as outfile, open("data.tsv","r") as f:
firstline = f.readline()
columns = firstline.split()
lines = f.readlines()[1:]
for line in lines:
    values = line.split()
    entry = dict(zip(columns, values))
    data.append(entry)
json.dump(data, outfile)