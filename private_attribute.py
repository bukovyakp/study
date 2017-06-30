#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):                 # Вызывается self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value                 # Self.attrname = value
                                                            # вызовет зацикливание!
class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'
    print (x.name)
    #y.name = 'Tom'                                          # <== ошибка

    y.age = 30
    print (y.age)
    #x.age = 40                                              # <== ошибка
