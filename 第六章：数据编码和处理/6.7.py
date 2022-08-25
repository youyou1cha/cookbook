#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 二进制数组的结构化数据到python元组中

from struct import Struct


def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures
    '''

    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Eample
if __name__ == '__main__':
    records = [
        (1, 2.3, 4.5),
        (6, 7.8, 9.0),
        (12, 13.4, 56.7)
    ]

    with open('data.b','wb') as f:
        write_records(records,'<idd',f)

def read_records(format,f):
    record_struct = Struct(format)
    chunks = iter(lambda : f.read(read_records.size),b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


