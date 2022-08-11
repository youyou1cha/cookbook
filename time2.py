#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 日期 datetime string str
"""
Topic: 最后的周五
Desc:
"""
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_preious_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

if __name__ == '__main__':
    datetime.today()
    print(get_preious_byday('Monday'))
    print(get_preious_byday('Tuesday'))
    print(get_preious_byday('Friday'))

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)

print(d + relativedelta(weekday=FR))
print(d + relativedelta(weekday=FR(-1)))

# strftime datetime -> str
# strptime str -> datetime
from datetime import datetime
dtext = '2012-09-20'
y = datetime.strptime(dtext,'%Y-%m-%d')
print(y)
z = datetime.now()
print(z - y)
strz = datetime.strftime(z,'%A %B %d %Y')
print(strz)