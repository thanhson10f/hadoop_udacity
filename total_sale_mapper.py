#!/usr/bin/python

import sys

for line in sys.stdin:
    info = line.strip().split("\t")
    if len(info)==6:
	date, time, store, category, sale, type = info
	print sale
