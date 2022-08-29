#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass

# user = getpass.getuser()
# user = 1
# passwd = getpass.getpass()

# def login(user,passwd):
#     if passwd == '1':
#         return True
#
# if login(user,passwd):
#     print('Yaj!')
# else:
#     print('Boo!')

import os
sz = os.get_terminal_size()
print(sz)