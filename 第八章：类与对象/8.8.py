#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 混入类 
# 添加日志，唯一性设置，类型检查

class LoggedMappingMixin:
    """
    add logging to get/set/delete operatins for debugging
    """
    
    def __getitem__(self, item):
        print('Getting' + str(item))
        return super().__getitem__(item)
    
    def __setitem__(self, key, value):
        print('Setting {}={!r}'.format(key,value))
        return super().__setitem__(key,value)
    
    def __delitem__(self, key):
        print('Deleting' + str(key))
        return super().__delitem__(key)
    

class SetOnceMappingMixin:
    
    __slots__ = ()
    
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key,value)
    
class StringKeysMappingMixin:
    
    __slots__ = ()
    
    def __setitem__(self, key, value):
        if not isinstance(key,str):
            raise TypeError('key must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key,value)

# 类装饰器
def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self,key):
        print('Getting' + str(key))
        return cls_getitem(self,key)

    def __setitem__(self,key,value):
        pass