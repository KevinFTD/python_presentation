#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年3月23日

@author: kevinftd
'''

# OOP style
class UpperAttrMetaclass(type):

    def __new__(self, name, bases, dct):
        # __new__ is the method called before __init__
        # it's the method that creates the object and returns it
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return super(UpperAttrMetaclass, self).__new__(self, name, bases, uppercase_attr)

class Foo():
    __metaclass__ = UpperAttrMetaclass

    bar = 'bip'

print hasattr(Foo, 'bar')
# Out: False
print hasattr(Foo, 'BAR')
# Out: True
