# coding=utf8

from streams import Processor

class UpperCase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys
    """
    виведення даних у потік stdout
    """
    obj = UpperCase(open('spam.txt'), sys.stdout)
    obj.process()
    """
    виведення даних у файл
    """
    prog = UpperCase(open('spam.txt'), open('spamp.txt', 'w'))
    prog.process()
