# coding: utf-8

"""
В следующем файле classexc.py определяется суперкласс с именем
General и два подкласса с именами Specific1 и Specific2. Этот пример иллюстри-
рует понятие категорий исключений, где General – это имя категории, а два под-
класса – это определенные типы исключений внутри категории. Обработчики,
которые перехватывают исключение General, так же будут перехватывать и все
его подклассы, в том числе Specific1 и Specific2:
"""

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()                   # Возбуждает экземпляр сеперкласса исключения
    raise X

def raiser1():
    X = Specific1()                 # Возбуждает экземпляр подкласса исключения
    raise X

def raiser2():
    X = Specific2()                 # Возбуждает другого подкласса исключения
    raise X


for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:                 # Перехватывает исключения General и любые его подклассы
        import sys
        print('caught:', sys.exc_info()[0])
