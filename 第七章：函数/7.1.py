#!/usr/bin/env python
# -*- coding: utf-8 -*-

def apply_ascyn(func, args, callback):
    '''

    '''
    result = func(*args)
    callback(result)


def add(x, y):
    return x + y


def print_result(result):
    print(result)


apply_ascyn(add, (2, 9), callback=print_result)
