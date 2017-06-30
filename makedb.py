#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
сохраняет объекты Person в хранилище
"""

import shelve

from Person import Person, Manager

bob = Person('Bob Smith')                               # Создание объектов для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')            # Имя файла хранилища
for obj in (bob, sue, tom):             # В качестве ключа использовать атрибут name
    db[obj.name] = obj                  # Сохранить объект в хранилище
db.close()                              # Закрыть после внесения изменений
