#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inspect import Signature, Parameter


def make_sig(*names):
    parms = [
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names
    ]
    return Signature(parms)


class StructureMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']
