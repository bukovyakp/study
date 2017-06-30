# coding: utf-8

"""
Например, в  следующем фрагменте, когда производится попытка получить
значение атрибута X.attr, интерпретатор автоматически вызывает метод __
get__ класса Descriptor, который присвоен атрибуту Subject.attr класса (как
и в случае со свойствами, в Python 2.6 класс дескриптора должен наследовать
суперкласс object – в Python 3.0 это наследование подразумевается по умолча-
нию, хотя его указание и не повредит)
"""


class Descriptor(object):
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')


class Subject:
    attr = Descriptor()                 # Атрибут класса – экземпляр класса Descriptor


X = Subject()
X.attr
print('-' * 10)
Subject.attr

print('=' * 40)

"""
Ниже приводится определение дескриптора, который управляет
доступом к  атрибуту name в  клиентском классе. Для доступа к  данным в  объ-
екте экземпляра, где фактически сохраняется строка с именем, его методы ис-
пользуют аргумент instance. Подобно свойствам дескрипторы корректно рабо-
тают, только когда они определяются как классы нового стиля и подключаются
к классам нового стиля, поэтому, если вы пользуетесь Python 2.6, не забудьте
добавить суперкласс object в определения обоих классов
"""

class Name(object):
    """Name descriptor docs"""
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')
        instance._name = value

    def __delete__(self, instance):
        print('remove...')
        del instance._name


class Person(object):
    def __init__(self, name):
        self._name = name

    name = Name()               # Присвоить атрибуту дескриптор


bob = Person('Bob Smith')       # Объект bob имеет управляемый атрибут
print(bob.name)                 # Вызовет Name.__get__
bob.name = 'Robert Smith'       # Вызовет Name.__set__
print(bob.name)
del bob.name                    # Вызовет Name.__delete__

print('-' * 20)
sue = Person('Sue Jones')       # Объект sue также наследует дескриптор
print(sue.name)
print(Name.__doc__)             # Или: help(Name)
