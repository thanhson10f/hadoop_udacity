#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	log_line = line.strip()
	match = re.search(r'\"\w+\s(\S+)', log_line)
	if match:
		print match.group(1)
