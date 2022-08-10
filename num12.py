#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 这么简单，我以前怎么想不到呢
# 输入两个字典，ChainMap() 返回连个dict的合并；实际是创建了一个能够存储这些字典的列表

from collections import ChainMap

a = {'x': 1, 'y': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a,b)
