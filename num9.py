#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 过滤序列；看了这一章节就是对序列字典的一些操作和总结
# 过滤 列表推导式、生成式、lambda、filter

# 列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
# lambad
print(list(filter(lambda x: x > 0,mylist)))
# 生成器
print((n for n in mylist if n > 0 ))
# filter
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
isvales = list(filter(is_int,values))

# 字典推导式
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = dict((key,value) for key ,value in prices.items() if value > 200)
p2 = {key:value for key,value in prices.items() if value >200 }

tech_name = {'APPL','IBM','HPQ','MSFT'}
p3 = {key: value for key ,value in prices.items() if key in tech_name}