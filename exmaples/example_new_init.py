#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年3月23日

@author: kevinftd

__new__创建类实例，__init__做初始化
'''

class base(object):
    def __init__(self, arg="base"):
        self.str = arg
    def __str__(self):
        return self.str

class strings(base):
    def __init__(self, arg=""):
        base.__init__(self, "%s__post"%(arg))

print strings()
print strings("abc")

##################


class inch1(float):
    "Convert from inch to meter"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)

print inch1(12)

class inch2(float):
    def __init__(self, arg=0.0):
        float.__init__(self, arg*0.0254)

print inch2(12) # just 12, because __init__ in float does nothing

