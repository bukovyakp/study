# __author__ = 'pavel'
# coding: utf-8

def count(aClass):
    aClass.numinstances = 0
    return aClass                   # Возвращает сам класс, а не обертку

@count
class Spam: pass                    # То же, что и Spam = count(Spam)

@count
class Sub(Spam): pass               # Инструкция numInstances = 0 не нужна здесь
