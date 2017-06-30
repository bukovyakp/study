# coding=utf8

class Number:
    def __init__(self, start):              # Вызов Number(start)
        self.data = start

    def __sub__(self, other):               # Выражение: экземпляр - other
        return Number(self.data - other)    # Результат – новый экземпляр

    def __str__(self):
        return self + 'test string'


if __name__ == '__main__':
    X = Number(5)
    Y = X - 2
    print(X.data)
    print('data')

