#!/usr/bin/env python
# -*- coding: utf-8 -*-

# __reversed__ 翻转实现

class Countdown:

    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n < self.start:
            yield n
            n += 1
if __name__ == '__main__':
    for rr in reversed(Countdown(10)):
        print(rr)

    for rr in Countdown(10):
        print(rr)