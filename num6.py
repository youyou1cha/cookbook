#!/usr/bin/env python
# -*- coding: utf-8 -*-

# slice indices

# 介绍slice 和indices的用法

SHARES = slice(20,23)
PIRCE = slice(31,37)

record = '....................100 .......513.25 ..........'
cost = int(record[SHARES] * float(record[PIRCE]))

# indices 就是引用切片，大的不动 小的取最小
a = slice(5,50,2)
s = 'HelloWorld'
a.indices(len(s)) # 返回元组