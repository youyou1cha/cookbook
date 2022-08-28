#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

class A:

    # Decorator as an instance method
    def decorator(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('decorator 1')
            return func(*args,**kwargs)
        return wrapper

    @classmethod
    def decorator2(cls,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 2')
            return func(*args,**kwargs)
        return wrapper

class Person:
    # Create a property instance
    first_name = property()

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name = value
