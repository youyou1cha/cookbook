#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 字符串匹配除了基本的find endswith startswith,主要
# 还是使用re。
# re的常用方法 re.compile 编译。re.match 匹配开头
# re.findall() re.finditer

text1 = '11/27/2021'
text2 = 'Nov 27,2021'

import  re

datepat = re.compile(r'\d+/\d+/\d+')
if re.match(r'\d+/\d+/\d+',text1):
    print('Yes')
else:
    print('No')

if datepat.match(text2):
    print('Yes')
else:
    print('No')
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.match(text3))
if datepat.match(text3):
    print('Yes')
print(datepat.findall(text3))

datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat2.match(text1))
print(datepat2.findall(text3))
print(list(datepat2.finditer(text3)))
# print([ m.group() for m in datepat2.match(text3) ])
m = datepat.match(text3)
print(m)

# re.match 从头开始匹配。group取出结果
# re.compile 编译正则
# re.search 扫描整个字符串。返回第一个 失败None
# re.findall 返回一个列表，失败空列表
# re.finditer 返回迭代器