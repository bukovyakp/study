# coding=utf8

from __future__ import print_function


class SkipIterator:
    def __init__(self, wrapper):
        self.wrapper = wrapper                  # информация о состоянии
        self.offset = 0

    def next(self):
        if self.offset >= len(self.wrapper):    # завершить итерации
            raise StopIteration
        else:
            item = self.wrapper[self.offset]    # иначе перешагнуть и вернуть
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapper):
        self.wrapper = wrapper                  # сохранить используемый элемент

    def __iter__(self):
        return SkipIterator(self.wrapper)       # каждий раз новый итератор

if __name__ == '__main__':
    alpha = 'temporary'
    skipper = SkipObject(alpha)                 # создать обьект-контейнер
    I = iter(skipper)                           # создать итератор для него
    print(next(I), next(I), next(I))            # обойти элементы 0, 2, 4

    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
