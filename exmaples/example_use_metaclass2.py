#!/usr/bin/env python2.7
#encoding=utf-8
"""
Created on 2015年3月23日

@author: kevinftd
"""

def ma(cls):
    # should take at least ONE argument to be a class method
    print "method a"

def mb(cls):
    print "method b"

method_dict={
    "ma":ma,
    "mb":mb,
}

class DynamicMethod(type):
    def __new__(cls,name,bases,attrs):
        if name[:3]=="Abc":
            attrs.update(method_dict)
        return type.__new__(cls,name,bases,attrs)

    def __init__(cls,name,bases,attrs):
        super(DynamicMethod,cls).__init__(name,bases,attrs)

class AbcTest(object):
    __metaclass__=DynamicMethod
    def mc(self,x):
        print x*3

class NotAbc(object):
    __metaclass__=DynamicMethod
    def md(self,x):
        print x*3

class Havemata(object):
    pass
class Nometa():
    pass

def main():
    a=AbcTest()
    a.mc(3)
    a.ma()
    print dir(a)

    b=NotAbc()
    print dir(b)

    print type(Havemata)
    print type(Nometa)

if __name__=="__main__":
    main()

