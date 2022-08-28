#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 带参数的装饰器函数

from functools import wraps,partial
import logging

def attach_wrapper(obj,func=None):
    if func is None:
        return partial(attach_wrapper,obj)
    setattr(obj,func.__name__,func)
    return func

def attach_wrappe(obj):
    @wraps(obj)
    def decorator(func):

        setattr(obj, func.__name__, func)
        @wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            return result
        return func
    return decorator

def att(obj):
    @wraps(obj)
    def wrapper(func):
        setattr(obj,func.__name__,func)
        return func
    return wrapper


def loggen(level,name=None,message=None):

    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)

        @attach_wrappe(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrappe(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

@loggen(logging.DEBUG)
def add(x,y):
    return x + y

@loggen(logging.CRITICAL,'example')
def spam():
    print('Spam')

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    add(2,3)
    add.set_message('ADD called')