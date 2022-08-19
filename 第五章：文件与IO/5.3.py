#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pickle 序列化
# import pickle
# data = 'a' # Some Python
# f = open('somefile','wb')
# pickle.dump(data,f)

import time
import threading

class Countdown:

    def __init__(self,n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):


    def start(self):