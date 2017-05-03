#!/usr/bin/python

import sys

count = 0
old_link = None
popular_link = None
popular_count = 0

for line in sys.stdin:
    link = line.strip()
    if old_link and old_link != link:
        if count > popular_count:
            popular_link = old_link
            popular_count = count
        count = 0

    old_link = link
    count = count + 1

if old_link and count > popular_count:
    pupular_link = old_link
    popular_count = count

print "{0}\t{1}".format(popular_link, popular_count)
