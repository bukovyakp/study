#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Функцию countLines(name), которая читает входной файл и подсчитывает
число строк в нем (подсказка: большую часть работы можно выполнить
с помощью метода file.readlines, а оставшуюся часть – с помощью функ-
ции len).

Все три функции в модуле mymod должны принимать имя файла в виде стро-
ки. Если размер любой из функций превысит две-три строки, это значит, что
вы делаете лишнюю работу
"""

def count_lines(filename):
    """
    Функцию countLines(name), которая читает входной файл и подсчитывает
    число строк в нем (подсказка: большую часть работы можно выполнить
    с помощью метода file.readlines, а оставшуюся часть – с помощью функ-
    ции len).
    """
    line_list = [line for line in open(filename).readlines()]
    return len(line_list)

def count_lines_2(filename):
    """
    функція count_lines реалізована в одну строку
    """
    return sum(1 for line in open(filename).readlines())

def count_lines_3(filename):
    file = open(filename, 'r')
    return len(file.readlines())

def count_chars(filename):
    """
    Функцию countChars(name), которая читает входной файл и подсчитыва-
    ет число символов в нем (подсказка: метод file.read возвращает единую
    строку)
    """
    return sum(1 for line in open(filename).read())


def count_lines_obj(object):
    """
    на вхід приймає об"єкт файлу. За допомогою цієї функції і наступної count_chars_obj у цьому ж можулі
    можна передавати функції об"єкт файлу, переставляючи каретку на початок файлу file.seek(0, 0)
    і відкривати файл лише один раз
    :param object:
    :return:
    """
    print('Count of lines ->')
    return sum(1 for line in object.readlines())

def count_chars_obj(object):
    """
    на вхід приймає об"єкт файлу. За допомогою цієї функції і count_lines_obj у цьому ж модулі
    можна передавати функції об"єкт файлу, переставляючи каретку на початок файлу за допомогою file.seek(0, 0)
    і відкривати файл лише один раз
    :param object:
    :return:
    """
    print('Count of symbols ->')
    return sum(1 for line in object.read())

def test(name):
    file = open(name, 'r')
    print(count_lines_obj(file))
    file.seek(0, 0)
    print(count_chars_obj(file))


if __name__ == '__main__':
    file = open('mymod.py', 'r')
    print(count_lines_obj(file))
    file.seek(0, 0)
    print(count_chars_obj(file))
