#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月1日

@author: kevinftd
'''

def framework(logic):
    try:
        print "[FX] start Framework..."
        it = logic()
        print "[FX] Framework call next()..."
        s = next(it)
        print "[FX] get next() return: ", s
        print "[FX] send(Goodnight, %s)"%(s)
        it.send("Goodnight, " + s)
    except StopIteration:
        print "[FX] StopIteration"

# Using a yield expression in a function definition will
# create a generator function instead of a normal function.
# will not be called until next called
def func():

    name = "Tom"
    print "[LOGIC] return '%s'.."%(name,)
    r = yield name
    print "[LOGIC] %s"%(r,)

    print '[LOGIC] Goodbye'
    # when this function is over, it will raise StopIteration

framework(func)
