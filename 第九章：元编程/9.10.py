#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Spam:

    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


s = Spam()
s.bar(2, 3)
s.bar('heelo')


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    return prop

class Person:
    name = typed_property('name',str)
    age = typed_property('age',int)

    def __init__(self,name,age):
        self.name = name
        self.age = age

from functools import partial

String = partial(typed_property,expected_type=str)
Integer = partial(typed_property,expected_type=int)

class Person1:
    name = String('name')
    age = Integer('age')

    def __init__(self,name,age):
        self.name = name
        self.age = age