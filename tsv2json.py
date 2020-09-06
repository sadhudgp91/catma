# Author: Kaushik Sadhu
# Script for TSV to JSON format conversion
# IMS - University of Stuttgart 15.08.2020
# Updated: September 06/2020
# filename = enter the tsv filename in cmd when you start conversion command by calling python tsv2Json.py "filename"


# Import lib

import csv
import json
import collections
import sys


# aliases
OrderedDict = collections.OrderedDict

src = '/tmp/data.log'
dst = '/tmp/data.json'

# data input output

data=[{}]
filename = sys.argv[1]
with open(filename,"r") as f:
    firstline = f.readline()
    columns = firstline.split()
    lines = f.readlines()[1:]
for line in lines:
    values = line.split()
    entry = dict(zip(columns, values))
    data.append(entry)
with open('output_TSV2JSON.json', 'w') as outfile:
    json.dump(data, outfile)