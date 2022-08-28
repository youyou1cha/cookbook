#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 带参数的装饰器的两种写法
# 1

import logging
import functools

def logger(msg=None):

    '''
    do somthongs
    '''

    def dector(func):
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            logging.info(func.__name__ + func.__doc__)
            logging.info(f"参数：{args}{kwargs}")
            if msg:
                logging.info(msg.format(result))
            return result
        return wrapper
    return dector

import logging
import functools

def logger(func=None,msg=None):

    if func is None:
        return functools.partial(logger,msg=msg)

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        logging.info(func.__name__ + func.__doc__)
        logging.info(f"lll")
        if msg:
            logging.info(msg.format(result))
        return result
    return wrapper