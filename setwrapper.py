# __author__ = 'pavel'
# coding: utf-8

class Set:
    def __init__(self, value=[]):           # Конструктор
        self.data = []                      # Управляет списком
        self.concat(value)

    def intersect(self, other):             # other – любая последовательность
        res = []                            # self – подразумеваемый объект
        for x in self.data:
            if x in other:                  # Выбрать общие элементы
                res.append(x)
        return Set(res)                     # Вернуть новый экземпляр Set

    def union(self, other):                 # other – любая последовательность
        res = self.data[:]                  # Копировать список
        for x in other:                     # Добавить элементы из other
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):                # Аргумент value: список, Set...
        for x in value:                     # Удалить дубликаты
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)                   # len(self)

    def __getitem__(self, kay):
        return self.data[kay]                   # self[i]

    def __and__(self, other):
        return self.intersect(other)            # self & other

    def __or__(self, other):
        return self.union(other)                # self | other

    def __repr__(self):
        return 'Set: ' + repr(self.data)        # Вывод


class NewSet(Set):
    """
    Теперь расширьте класс множества наследованием, чтобы подкласс мог
    обрабатывать произвольное число операндов, используя для этого форму
    аргумента *args. (Подсказка: вернитесь к рассмотрению этих алгоритмов
    в  главе  18.) Найдите пересечение и  объединение нескольких операндов
    с помощью вашего подкласса множества. Как можно реализовать вычис-
    ление пересечения трех и более множеств, если оператор & работает всего
    с двумя операндами?
    """
    def __init__(self, *args):
        self.data = []
        self.concat(*args)

    def concat(self, *args):                # Аргументы args: список, Set...
        for x in args:                      # Удалить дубликаты
            if not x in self.data:
                self.data.append(x)

if __name__ == '__main__':
    x = Set([1, 3, 5, 5, 7])
    r = Set([1, 4, 7, 8])
    print (x)
    print (r)
    print('\tx.union(r) -->  %s' % (x.union(r)))
    print(x | Set([1, 4, 6, 9]))
    print(r[2])

    X = NewSet('test', 'two', 'three')
    Y = NewSet('two', 'five', 'six')
    print(X & Y)
    print(X | Y)
