#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类创建的所有步骤；__prepare__() 的方法创建命名。通常返回一个映射对象或者字典
# __new__() 实例化类对象。在类主体执行完以后开始执行
# __init__() 最后调用。最后执行一些初始化工作

# Signature Parameter

from inspect import Signature,Parameter

parms = [
    Parameter('x',Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y',Parameter.POSITIONAL_OR_KEYWORD,default=42),
    Parameter('z',Parameter.KEYWORD_ONLY,default=None)
]
sig = Signature(parms)
print(sig)

def func(*args,**kwargs):
    bound_values = sig.bind(*args,**kwargs)
    for name ,value in bound_values.arguments.items():
        print(name,value)

func(1,2,z=3)