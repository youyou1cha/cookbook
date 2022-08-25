#!/usr/bin/env python
# -*- coding: utf-8 -*-


def apply_async(func,args,callback):
    result = func(*args)
    callback(result)

def add(x,y):
    return x + y

def make_handle():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}]  Got :{}'.format(sequence,result))

handle = make_handle()
next(handle)
apply_async(add,(3,3),callback=handle.send)