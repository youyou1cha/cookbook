#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字典的最大最小值

# 通过zip方法 和sorted
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))

# 2
min(prices,key=lambda  K:prices[k])
max(prices,key=lambda K:prices[k])
min(prices.keys())
max(prices.values())

# 字典中选择相同点
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}
# 字典的keys和items支持字典set操作
a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()