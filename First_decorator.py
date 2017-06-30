# __author__ = 'pavel'
# coding: utf-8

class Tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('Calls %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@Tracer
def spam(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam('a', 'b', 'c')
    spam(4, 5, 6)
