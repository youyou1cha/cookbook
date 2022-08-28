#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 包装器
# 装饰器 和包装器有啥区别

import time
from functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

# 略过装饰器
# __wrapped__方法；