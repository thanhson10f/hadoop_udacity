#!/usr/bin/python

import sys

count = 0
old_link = None
for line in sys.stdin:
    link = line.strip()
    if old_link and old_link != link:
        print "{0}\t{1}".format(old_link, count)
        count = 0

    old_link = link
    count = count + 1

if old_link:
    print "{0}\t{1}".format(old_link, count)
