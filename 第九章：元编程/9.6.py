#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 单例模式
# metaclass

class Singletion(type):
    def __init__(self,*args,**kwargs):
        self.__instance = None
        super().__init__(*args,**kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super(Singletion, self).__call__(*args,**kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singletion):
    def __init__(self):
        print('Creatinng Span')



import weakref

class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakKeyDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super(Cached, self).__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam(metaclass=Cached):
    def __init__(self,name):
        print('Creating Spam({!r})'.format(name))
        self.name = name