#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月2日

@author: kevinftd
'''

class A(object):
    def __init__(self):
        print "A __init__"
        super(A, self).__init__()

class B(object):
    def __init__(self):
        print "B __init__"
        super(B, self).__init__()

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

instance = C()

# output:
# A __init__
# B __init__
# B __init__

print C.__mro__ # method resolution order
