#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	log_line = line.strip()
	match = re.search(r'\"\w+\s(\S+)', log_line)
	if match:
		path = match.group(1)
        path = path.replace('http://www.the-associates.co.uk','')
        print path
