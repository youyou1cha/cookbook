#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 匿名类类似的功能 nametuple
# 默认是不可以修改属性。但是可以用_replace方法

from collections import  namedtuple

Subscriber = namedtuple('Subscriber',['name','joined'])
Sub = Subscriber('jojo','20200101')
print(Sub)