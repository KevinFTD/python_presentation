#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年3月23日

@author: kevinftd

继承后的__init__和__new__
'''

class Base(object):
    def __new__(cls, *args, **kwargs):
        print "__new__ in Base"
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        print "__init__ in Base"

class Example(Base):
    def __new__(cls, *args, **kwargs):
        print "__new__ in Example"
        return Base.__new__(cls, *args, **kwargs)

    def __init__(self):
        print "__init__ in Example"
        Base.__init__(self)

instance = Example()
