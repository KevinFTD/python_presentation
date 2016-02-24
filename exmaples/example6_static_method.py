#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月16日

@author: kevinftd
'''

class My_cls(object):
    data = 10

    @staticmethod
    def static_method():
        print My_cls.data

    @classmethod
    def class_method(cls):
        print cls.data

class Child_cls(My_cls):
    data = 20

My_cls.static_method()
My_cls.class_method()

Child_cls.static_method()
Child_cls.class_method()
