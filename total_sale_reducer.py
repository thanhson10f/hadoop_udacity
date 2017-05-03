#!/usr/bin/python
import sys

count = 0
total_sale = 0

for line in sys.stdin:
    info = line.strip() 
    sale = float(info)
    total_sale = total_sale + sale
    count = count + 1

print "{0}\t{1}".format(count, total_sale)
