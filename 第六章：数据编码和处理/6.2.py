#!/usr/bin/env python
# -*- coding: utf-8 -*-
# json 序列化成python对象
import json

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict

# object_pairs_hook 有序键值
# object_hook 无序
data = json.loads(s,object_pairs_hook=OrderedDict)
print(data)  # OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])

class JSONObject:
    def __init__(self,d):
        # __dict__ 就是类属性
        self.name = d['price']

data = json.loads(s,object_hook=JSONObject)
print(vars(data))

# 序列化对象成json
def serialize_instance(obj):
    d = {'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d

# dict -> object
def unserialize_object(d):
    clsname = d.pop('__classname__',None)
    if clsname:
        obj = clsname.__new__(clsname)
        for key,value in d.items():
            setattr(obj,key,value)
        return obj
    else:
        return d

import sys
import json

class Person:
    def __init__(self,data=None):
        self._name = '1'
        self._sex = ""
        self._blood_type = "0"
        self._hobbies = []

        self._date_of_birth = '111'
    if data:
        self.__dict__ = data

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_if_birth(self,date_of_birth):
        self._date_of_birth = date_of_birth

def main():
    try:
        str1 = '{"name": "Tom", "sex": "male", "blood_type": "A", "hobbies": ["篮球", "足球"]}'
        person1 = json.loads(str1,object_hook=Person)
        print(isinstance(person1,Person))
    except Exception as e:
        pass
