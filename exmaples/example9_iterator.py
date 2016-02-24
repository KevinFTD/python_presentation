#!/usr/bin/env python2.7
#encoding=utf-8
'''
Created on 2015年4月22日

@author: kevinftd
'''

class Data(object):
    def __init__(self):
        self._data = [1, 2, 3, 4]
        self._index = 0

    def __iter__(self):
        return self

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration
        d = self._data[self._index]
        self._index += 1

        return d

data_instance = Data()

for data in data_instance:
    print data

class Data2(object):
    def __init__(self):
        self._data = [1, 2, 3, 4]

    def __iter__(self):
        for d in self._data:
            yield d

data_instance = Data2()

for data in data_instance:
    print data
