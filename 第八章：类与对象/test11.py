#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections.abc import  Iterator

def list_items_to_items(items):

    for item in items:
        if isinstance(item,Iterator):
            yield from item
        else:
            yield item


a = [1,2,3,['1',[2,3,4],'a'],['a','b',['c',['d','1',[2,3,4],'a'],['a','b',['c',['d']],['c',['c','d']]]]]]

import itertools
out = list(itertools.chain.from_iterable(a))
print(out)

