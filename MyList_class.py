# __author__ = 'pavel'
# coding: utf-8

from sys import stdout as stdout

class MyList(list):
    """
    Перегрузка операторов. Напишите класс с  именем MyList, который «обер­
    тывает» списки языка Python: он должен перегружать основные операторы
    действий над списками, включая +, доступ к элементам по индексу, итера-
    ции, извлечение среза и  такие методы списка, как append и  sort. Полный
    перечень методов, поддерживаемых списками, вы найдете в справочном ру-
    ководстве по языку Python. Кроме того, напишите конструктор для своего
    класса, который принимает существующий список (или экземпляр класса
    MyList) и копирует его в атрибут экземпляра.
    """
    def __init__(self, value):
        list.__init__([])               # Адаптирует список
        self.concat(value)

    def add(self, other):
        res = MyList(self)              # Копіюємо початковий список
        res.concat(other)
        return MyList(res)              # повертаємо результуючий список

    def concat(self, value):
        for x in value:
                self.append(x)

    def __add__(self, val):
        return self.add(val)

    def __getitem__(self, item):        # Перегрузка доступа к элементам по индексу
        # print('(indexing %s at %s  --> %s)' % (self, item, list.__getitem__(self, item - 1)))
        return list.__getitem__(self, item)

    def __iter__(self):                 # Перегрузка метода итераций
        print('iteration implementing')
        return list.__iter__(self)


class MyListSub(MyList):
    """
    Подклассы. Напишите подкласс с  именем MyListSub, наследующий класс
    MyList из упражнения 2, который расширяет класс MyList возможностью
    вывода сообщения на stdout перед выполнением каждой перегруженной
    операции и  подсчета числа вызовов. Класс MyListSub должен наследовать
    методы MyList. При сложении MyListSub с последовательностями должно вы-
    водиться сообщение, увеличиваться счетчик вызовов операции сложения
    и вызываться метод суперкласса. Кроме того, добавьте новый метод, кото-
    рый будет выводить счетчики операций на stdout, и поэкспериментируйте
    с этим классом в интерактивной оболочке. Как работают ваши счетчики –
    считают ли они операции для всего класса (для всех экземпляров класса)
    или для каждого экземпляра в отдельности? Как бы вы реализовали каж-
    дый из этих случаев? (Подсказка: зависит от того, в каком объекте произво-
    дится присваивание значения счетчика: атрибут класса используется все-
    ми экземплярами, а атрибуты аргумента self хранят данные экземпляра.)
    """
    NumRequests = 0

    @staticmethod                                                     # декоратор статического метода класса
    def print_num_requests():
        print('Number of instances created: ', MyListSub.NumRequests)

    def __getattr__(self, item):
        stdout.write('Хрен тобі, а не такий атрибут :)\n')

    def __setattr__(self, attr, value):
        stdout.write('Хюстон викликає атрибут: " {0} " і присвоює йому значення: {1}\n'.format(attr, value))
        MyListSub.NumRequests += 1
        MyListSub.print_num_requests()
        self.__dict__[attr + '_usr'] = value

    def add(self, other):
        stdout.write('Implementing "add" method of MyListSub class')
        MyListSub.NumRequests += 1
        MyList.add(self, other)


if __name__ == '__main__':
    x = MyList([1, 2, 3, 4, 5])
    y = MyList([10, 20, 30, 40])
    print(x + y)
    print([1, 2, 3] + x)

    z = MyListSub([100, 200, 300])
    f = MyListSub([100, 200, 300])
    r = MyListSub([100, 200, 300])
    print(z[1:2])
    z.data = 1
    z.reset
    z.add([20, 30])
    f.add([20, 30])
    r.add([20, 30])
    z.print_num_requests()





