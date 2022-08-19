#!/usr/bin/env python
# -*- coding: utf-8 -*-

# itertools.islice(迭代器，start,stop[,step])
# itertools.dropwhile()函数，穿衣一个函数对象，和迭代对象法，。返回一个迭代对象。丢弃原序列对象，直到函数返回false之前的所有元素

from itertools import dropwhile

with open('/etc/passwd') as f:
    for line in dropwhile(lambda line:not line.startswith('#'),f):
        print(line,end='')