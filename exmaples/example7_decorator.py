#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月16日

@author: kevinftd
'''

def hello(fn):

    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__

    return wrapper

@hello
def foo():
    print "i am foo"

foo()
