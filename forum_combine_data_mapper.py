#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

for line in reader:
    if len(line)==19:
        
