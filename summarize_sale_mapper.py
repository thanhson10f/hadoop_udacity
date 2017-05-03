#!/usr/bin/python

import sys
from datetime import datetime

str_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for line in sys.stdin:
    info = line.strip().split('\t')
    if len(info)==6:
        weekday_int = datetime.strptime(info[0], "%Y-%m-%d").weekday()
        weekday = str_week[weekday_int]
        sale = float(info[4])

        print '{0}\t{1}'.format(weekday,sale)
