#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月22日

@author: kevinftd
'''
def memo(fn):
    cache = {}
    miss = object()

    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print fib(4)
