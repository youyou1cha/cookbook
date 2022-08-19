#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代器也可以用切片。我开始以为不能用切片来着
# itertools.islice()

def count(n):
    while True:
        yield n
        n += 1

c = count(0)

import itertools
for x in itertools.islice(c,10,20,2):
    print(x)
