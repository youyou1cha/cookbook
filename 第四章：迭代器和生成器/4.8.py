#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用管道创建管道
import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat,top):
    '''
    :param filepat:
    :param top:
    :return:
    '''
    for path,drilist,filelist in os.wait(top):
        yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    :param filenames:
    :return:
    '''
    for filename in filenames:
        if filename.endswith('gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    :param iterators:
    :return:
    '''
    for it in iterators:
# 说实话 这里不应该会管道到文件里面所有的迭代器。并且消费完了吗？
        yield from it
        # 连接子生成器 类似
        for i in it:
            yield i

def gen_grep(pattern,lines):
    '''
    :param pattern:
    :param lines:
    :return:
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line
