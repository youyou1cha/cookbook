#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = [1,2,3,4,5,6,7,8,9]

def do():
    # for i in iter(t):
    print('start')
    yield from iter(t)
if __name__ == '__main__':
    t1 = do()
    t2 = next(t1)
    print(t2)