#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classtools import AttrDisplay                              # Импортирует обобщенный инструмент


class Person(AttrDisplay):
    """
    Создает и обрабатывает записи с информацией о людях
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):                                        # Предполагается, что фамилия
        return self.name.split()[-1]                            # указана последней

    def give_raise(self, percent):                              # Процент – величина в диапазоне 0..1
        self.pay = int(self.pay * (1 + percent))

'''    def __str__(self):
        return '[Person: %s is %s with pay: %s]' % (self.name, self.job, self.pay) '''

class Manager(Person):
    """
    Версия класса Person, адаптированная в соответствии
    со специальными требованиями
    """
    def __init__(self, name, pay):                              # Переопределенный конструктор
        Person.__init__(self, name, 'mgr', pay)                 # Вызов оригинального конструктора со значением
                                                                # 'mgr' в аргументе job

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)


class ManagerTwoVersion:
    """
    Альтернативная версия класса Manager с вложенным объектом
    """
    def __init__(self, name, pay):
        self.Person = Person(name, 'mgr', pay)

    def give_raise(self, percent, bonus=.10):
        self.Person.give_raise(percent + bonus)

'''    def __getattr__(self, attr):
        return getattr(self.Person, attr) '''

'''    def __str__(self):
        return str(self.Person)  '''


class Department:
    """
    Объединение объектов в составной объект
    """
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=10000)

    # print('{0} {1}'.format(bob.name, bob.pay))
    # print('{0} {1}'.format(sue.name, sue.pay))
    print(bob.last_name(), sue.last_name())
    print(bob)
    print(sue)
    sue.give_raise(0.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.give_raise(.10)
    print(tom.last_name())
    print(tom)
'''
    print('--- All three ---')
    for obj in (bob, sue, tom):
        obj.give_raise(.10)
        print(obj)
    development = Department(bob, sue)       # Встраивание объектов в составной объект
    development.add_member(tom)
    development.give_raises(.10)             # Вызов метода giveRaise вложенных объектов
    development.show_all()                   # Вызов метода __str__ вложенных объектов
'''