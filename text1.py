#!/usr/bin/env python
# -*- coding: utf-8 -*-
line = 'asdf fjdk; afed, fjek,asdf, foo'

import  re
# re.split() 捕获分组，匹配的文本也会出现在结果里面。如果不想(?:....)
print(re.split(r'[;,\s]\s*',line))
filelds = re.split(r'(;|,|\s)\s*',line)

value  = filelds[::2]
delimiters = filelds[1::2] + ['']
# zip 返回元组
d = ''.join(v+d for v,d in zip(value,delimiters))


#  startswith() endswith() 接受元组类型
# if any(name.endswith(('.c','py')) for name in listdir(dirname))