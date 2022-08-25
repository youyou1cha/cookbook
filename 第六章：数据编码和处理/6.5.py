#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python字典转xml格式
import typing
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
def dict_to_xml(tag:str,d:typing.Dict):
    '''
    Turn a simple dict of key/value pairs into xml
    '''
    elem = Element(tag)
    for key,value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem

