#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Iterable

def flattem(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield  from flattem(x)
        else:
            yield x

