# Author: Kaushik Sadhu
# Script for text file to JSON format conversion
# IMS - University of Stuttgart 15.08.2020
# Updated: September 06/2020
# filename = enter the tsv filename in cmd when you start conversion command by calling python txt2Json.py "filename"


# Import lib

import csv
import sys
import json
import collections

# aliases
OrderedDict = collections.OrderedDict

src = '/tmp/data.log'
dst = '/tmp/data.json'

# data input output

data=[]
filename = sys.argv[1]
with open(filename,'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write("token"+'\t'+"sentstart"+ '\n' + content)
with open(filename,"r") as f:
    firstline = f.readline()    
    columns = firstline.split()
    lines = f.readlines()[0:]
for line in lines:
    values = line.split()
    entry = dict(zip(columns, values))
    data.append(entry)
with open('Output_tokens.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys = False)
