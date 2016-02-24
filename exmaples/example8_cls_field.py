#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月7日

@author: kevinftd
'''

class MyClass(object):

    key1 = 10
    key2 = []

    def __init__(self):
        '''
        Constructor
        '''
        self.key1 = 20
        self.key2.append(30)

instance = MyClass()

print instance.key1
print MyClass.key1

print instance.key2
print MyClass.key2
