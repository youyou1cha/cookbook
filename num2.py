2#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  怎么从一个集合中获取最大或者最小的N个元素列表

# 通过list转成heapd。来获取

import heapq

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))