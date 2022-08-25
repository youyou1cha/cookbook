#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 数据库用sqlalchemy

# 十六进制字符串表示一个字节字符串；或者反过来
s = b'hello'
# Encode as hex
import binascii

h = binascii.b2a_hex(s)
print(h)