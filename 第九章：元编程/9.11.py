#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from contextlib import contextmanager

# yield 代码在上下文管理器作为__enter__()方法执行
# yield之后的代码作为__exit__()方法执行

@contextmanager
def timethis(lable):
    start = time.time()

    try:
        yield

    finally:
        end = time.time()
        print('{}:{}'.format(lable,end-start))

@contextmanager
def time1(lable):
    print('qian')
    yield
    print('hou')
    print(lable)

# with timethis('counting'):
#     n = 10000000
#     while n > 0’；、[''.。:
#         n -= 1]

# with time1('aaa'):
#     n = 111
#     while n > 0:
#         n -= 1
#
？

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working//
    / ‘；working