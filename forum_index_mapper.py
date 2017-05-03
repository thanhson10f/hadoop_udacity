#!/usr/bin/python

import sys
import re
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
for line in reader:
    node_id = line[0]
    body = line[4]

    words = re.findall(r"[\w'\\|+*&^%@`~]+", body)
    if words:
        for word in words:
            print '{0}\t{1}'.format(word.lower(),node_id)
