# __author__ = 'pavel'
# coding: utf-8

class Spam():
    numInstances = 0

    def count(cls):                 # Счетчик экземпляров для каждого отдельного класса
        cls.numInstances += 1       # cls – ближайший к экземпляру класс

    def __init__(self):
        self.count()                # Передаст self.__class__ для подсчета

    count = classmethod(count)


class Sub(Spam):
    numInstances = 0

    def __init__(self):             # Переопределяет __init__
        Spam.__init__(self)


class Other(Spam):                  # Наследует __init__
    numInstances = 0


if __name__ == '__main__':
    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print(x.numInstances, y1.numInstances, z1.numInstances)
    print(Spam.numInstances, Sub.numInstances, Other.numInstances)