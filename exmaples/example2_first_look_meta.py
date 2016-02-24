#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年3月24日

@author: kevinftd

class对象的创建
'''

def SimpleMeta(class_name, class_parents, class_attrs):
    print 'create class %s'%(class_name,)
    return type(class_name, class_parents, class_attrs)


class Example(object):
    __metaclass__ = SimpleMeta

