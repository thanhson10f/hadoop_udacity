#!/usr/bin/python

import sys

old = None
current_sale = 0
current_count = 0
for line in sys.stdin:
    info = line.strip().split('\t')
    weekday = info[0]
    sale = float(info[1])

    if old and old != weekday:
        print '{0}\t{1}'.format(old, current_sale/current_count*1.0)
        current_sale = 0
        current_count = 0

    old = weekday
    current_sale = current_sale + sale
    current_count = current_count + 1

if old:
    print '{0}\t{1}'.format(old, current_sale/current_count*1.0)
