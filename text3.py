#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 最短匹配模式 通过正则上加上？
import re
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'"(.*?)"')
str_pat1 = re.compile(r'"(.*)"')

print(str_pat.findall(text1))
print(str_pat1.findall(text1))
print(str_pat.findall(text2))
print(str_pat1.findall(text2))

# 多行匹配模式  re.DOTALL;用来匹配换行
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
