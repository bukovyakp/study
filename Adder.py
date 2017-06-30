# __author__ = 'pavel'
# coding: utf-8
"""

Наследование. Напишите класс с  именем Adder, экспортирующий метод
add(self, x, y), который выводит сообщение «Not Implemented» («Не реали-
зовано»). Затем определите два подкласса класса Adder, которые реализуют
метод add:


"""
class Adder:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        print('Reloaded method __add__')
        return self.add(self.data, other)

    def add(self, x, y):
        print('Not Implemented')


class ListAdder(Adder):
    """
    ListAdder
    С методом add, который возвращает результат конкатенации двух спи-
    сков из аргументов.
    реализуйте перегрузку оператора + с помощью метода
    __add__ так, чтобы он автоматически вызывал ваш метод add (например, вы-
    ражение X + Y должно приводить к вызову метода X.add(X.data, Y))
    """
    def add(self, x, y):
        print('My method add')
        return x + y


class DictAdder(Adder):
    """
    DictAdder
    С методом add, который возвращает новый словарь, содержащий элемен-
    ты из обоих словарей, передаваемых как аргументы (подойдет любое
    определение сложения).
    """
    def add(self, x, y):
        result = dict(x, **y)
        return result


if __name__ == '__main__':
    #    L = [10, 20, 30]
    X = [50, 60, 70]

    #    i = Adder(L)
    #    i.add('a', 'b')

    a = [1, 2, 3, 4]
    b = [6, 7, 8]
    r = ListAdder(X)
    print(r.data)
    print(r.add(a, b))
    r.a = a
    r.b = b
    print(r + r.b)

    dict1 = {'test': 2}
    dict2 = {'two': 4}
    dict_data = {'four': 5}
    func = DictAdder(dict_data)
    print(func.add(dict1, dict2))
    print(func + dict1)
