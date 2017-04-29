#!/usr/bin/python
import sys

highest_sale = 0
old_cat = None

for line in sys.stdin:
    info = line.strip().split("\t")
    if len(info)==2:
        this_cat, this_sale = info

        if old_cat and this_cat != old_cat:
            print "{0}\t{1}".format(old_cat, highest_sale)
            highest_sale = 0

        old_cat = this_cat
	if highest_sale < float(this_sale):
	    highest_sale  = float(this_sale)

if old_cat:
    print "{0}\t{1}".format(old_cat, highest_sale)
