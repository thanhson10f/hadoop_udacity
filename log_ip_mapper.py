#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    log = line.strip()
    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', log)
    if match:
        print match.group(1)
