__author__ = 'pavel'
# coding=utf8

"""
Ниже демонстрируется возможность сохранения четырех объектов связанных методов в списке
и их вызов как обычных функций:
"""

class Number:
    def __init__(self, base):
        self.base = base

    def double(self):
        return self.base * 2

    def triple(self):
        return self.base * 3

x = Number(2)                                       # Объекты экземпляров класса
y = Number(3)                                       # Атрибуты + методы
z = Number(4)

acts = [x.double, y.double, y.triple, z.double]     # Список связанных методов

for act in acts:                                    # Вызовы откладываются
    print(act())                                    # Вызов как функции

