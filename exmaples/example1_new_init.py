#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月15日

@author: kevinftd
'''

def trace(func):

    def inner(*args, **kwargs):
        print '{0} is called'.format(func.__name__)
        return func(*args, **kwargs)

    return inner

class My_cls(object):
    @trace
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

    @trace
    def __init__(self):
        pass

instance = My_cls()
