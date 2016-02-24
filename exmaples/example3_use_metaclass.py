#!/usr/bin/env python2.7
# encoding=utf-8
'''
Created on 2015年3月20日

@author: kevinftd
'''

# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(class_name, class_parents, class_attr):
    """
        Return a class object, with the list of its attribute turned
        into uppercase.
    """

    # pick up any attribute that doesn't start with '__'
    attrs = ((name, value) for name, value in class_attr.items() if not name.startswith('__'))
    # turn them into uppercase
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # let `type` do the class creation
    return type(class_name, class_parents, uppercase_attr)

__metaclass__ = upper_attr  # this will affect all classes in the module

class Foo():  # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'

print hasattr(Foo, 'bar')
# Out: False
print hasattr(Foo, 'BAR')
# Out: True

# but this class in the module not be affected
class Foo1(object):
    bar = 'bip'

f = Foo1()
print f.BAR
# Out: 'bip'
