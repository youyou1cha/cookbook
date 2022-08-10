#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用depue的固定大小的特点，保留最后元素
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)

    for line in lines:

        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    lines = '''
    aaaaaaaaaaaaaaaaaaaaa
    bbbbbbbbbbbbbbbbbbbbb
    ccccccccccccccccccccc
    ddddddddddddddddddddd
    eeeeeeeeeeeeeeeeeeeee
    aaaaaaaaaaaaaaaaaaaaa
    1111111111111
    2
    1
    da
    a
    a
    ad
    sd
    ad
    sad
    ad
    f
    dfdf
    gs
    aaa
    '''
    for line , prevlines in search(lines.replace('\\n','').split('  '),'aa',5):
        for pline in prevlines:
            print(pline,end='')
        print(line,end='')
        print('---' * 20)
