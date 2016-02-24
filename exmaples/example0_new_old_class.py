#encoding=utf-8
'''
Created on 2015年3月20日

@author: kevinftd

differences between new style class and old style class
'''

class New_cls(object):
    pass

class Old_cls():
    pass

class Old_2_cls(Old_cls):
    pass


if __name__ == '__main__':
    new = New_cls()
    old = Old_cls()

    # __dict__ 为属性名-属性的字典
    print "new.__dict__: ", new.__dict__
    print "old.__dict__: ", old.__dict__

    print "New_cls.__dict__: ", New_cls.__dict__
    print "Old_cls.__dict__: ", Old_cls.__dict__

    print "type(New_cls): ", type(New_cls)
    print "type(Old_cls): ", type(Old_cls)

    print "type(Old_2_cls): ", type(Old_2_cls)
