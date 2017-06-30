__author__ = 'pavel'
# coding=utf8



class ListInstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функций print() и str() с экземпляром в виде аргумента, через наследование
    метода __str__, реализованного здесь; отображает только атрибуты
    экземпляра; self – экземпляр самого нижнего класса в дереве наследования;
    во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __X
    """
    def __str__(self):
        return '< Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,                        # имя клиентского класса
            id(self),                                       # адресс экземпляра
            self.__attr_names())

    def __attr_names(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t name %s = %s\n' % (attr, self.__dict__[attr])
        return result


class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'


class ListInherited:
    """
    Использует функцию dir() для получения списка атрибутов самого экземпляра
    и атрибутов, унаследованных экземпляром от его классов; в Python 3.0
    выводится больше имен атрибутов, чем в 2.6, потому что классы нового стиля
    в конечном итоге наследуют суперкласс object; метод getattr() позволяет
    получить значения унаследованных атрибутов, отсутствующих в self.__dict__;
    реализует метод __str__, а не __repr__, потому что в противном случае
    данная реализация может попасть в бесконечный цикл при выводе связанных
    методов!
    """

    def __str__(self):
        return '< Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,                        # имя клиентского класса
            id(self),                                       # адресс экземпляра
            self.__attr_names())

    def __attr_names(self):
        result = ''
        for attr in dir(self):                              # Передать экземпляр функции dir()
            if attr[:2] == '__' and attr[-2:] == '__':      # Пропустить внутренние имена
                result += '\t name %s < >\n' % attr
            else:
                result += '\t name %s = %s\n' % (attr, getattr(self, attr))
        return result


class ListTree:
    """
    Примесный класс, в котором метод __str__ просматривает все дерево классов
    и составляет список атрибутов всех объектов, находящихся в дереве выше
    self; вызывается функциями print(), str() и возвращает сконструированную
    строку со списком; во избежание конфликтов с именами атрибутов клиентских
    классов использует имена вида __X; для рекурсивного обхода суперклассов
    использует выражение-генератор; чтобы сделать подстановку значений более
    очевидной, использует метод str.format()
    """

    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attr_names(self, 0),
            self.__list_class(self.__class__, 4))

    def __list_class(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__list_class(c, indent+4)
                        for c in aClass.__bases__)
            return '\n{0} Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attr_names(aClass, indent),
                ''.join(genabove),
                dots)

    def __attr_names(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result


class NewList(ListInstance, ListTree):
    def __str__(self):
        return self

    def super_class(self):
        return('\nInstance of {0}({1}), address {2} \n'.format(
            self.__class__.__name__,
            self.bases(),
            id(self)
        ))

    def bases(self):
        res = ''
        symbol = ', '
        number_of_passes = 0
        for name in self.__class__.__bases__:
            if number_of_passes == 0:
                res += name.__name__
                number_of_passes += 1
            else:
                res += symbol + name.__name__
        return res



if __name__ == '__main__':
    x = NewList()
    print(x)
    print(sorted(x.__dict__))
    a = NewList()
    print(a.super_class())
    print(a.__class__.__name__)

