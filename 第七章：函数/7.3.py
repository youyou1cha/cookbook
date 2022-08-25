#!/usr/bin/env python
# -*- coding: utf-8 -*-

def apply_async(func,args,callback):
    res = func(*args)

    callback(res)

def add(x,y):
    return x + y

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got:{}'.format(sequence,result))
    return handler

handle = make_handler()

apply_async(add,(2,3),callback=handle)