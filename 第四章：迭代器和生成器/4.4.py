#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用yield 可以把值复制给变量。把迭代器的变量值传给外部
# send 可以把外部的值传给内部
# yield from 就可以做到一种管道，做到流程转换

from collections import deque

class linehistory:

    def __init__(self,lines,histlen=3):
        self.line = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.line,1):
            self.history.append((lineno,line))
            yield line

    def clear(self):
        self.history.clear()