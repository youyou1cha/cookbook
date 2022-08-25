#!/usr/bin/env python
# -*- coding: utf-8 -*-

def apply_asyc(func,args,callback):
    result = func(*args)

    callback(result)

def add(x,y):
    return  x + y

class ResultHandle(object):
    def __init__(self):
        self.sequence = 0

    def handle(self,result):
        self.sequence += 1
        print('[{}] Got:{}'.format(self.sequence,result))

result_handle = ResultHandle()

apply_asyc(add,(2,3),callback=result_handle.handle)