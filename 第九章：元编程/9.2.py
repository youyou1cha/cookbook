#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 带参数的装饰器

from functools import wraps
import logging

def logged(level,name=None,message=None):
    """
    Add logging to a function
    """

    def decorate(func):
        logname = name if name else func.__module__
        # log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        logging.basicConfig(format='%(levelname)s:%(message)s', level=level)
        @wraps(func)
        def wrapper(*args,**kwargs):
            # log.log(level,logmsg)
            logging.info(logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate

@logged(logging.INFO)
def add(x,y):
    return x + y

@logged(logging.CRITICAL,'example')
def spam():
    print('Spam')

if __name__ == '__main__':
    a = add(1,2)
    print(a)
    # spam()