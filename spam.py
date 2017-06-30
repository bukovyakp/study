# __author__ = 'pavel'
# coding: utf-8

class Spam:
    NumInstances = 0

    def __init__(self):
        Spam.NumInstances += 1

    @staticmethod                                                     # декоратор статического метода класса
    def print_num_instances():
        print('Number of instances created: ', Spam.NumInstances)

    # print_num_instances = staticmethod(print_num_instances)         # Работает в обоих версиях 2.7 и 3.Х


class Sub(Spam):
    def print_num_instances():                                      # Переопределяет статический метод
        print('Extra stuff')
        Spam.print_num_instances()                                  # Который вызывает оригинал

    print_num_instances = staticmethod(print_num_instances)


class Other(Spam):
    pass


class SpamSecond():
    NumInstances = 0                                  # Вместо статического метода используется метод класса

    def __init__(self):
        SpamSecond.NumInstances += 1

    def print_num_instances(cls):
        print('Num instances: ', SpamSecond.NumInstances)

    print_num_instances = classmethod(print_num_instances)



if __name__ == '__main__':
    a = Spam()                                                      # создадим несколько екземпляров
    b = Spam()
    c = Spam()

    Spam.print_num_instances()

    d = Sub()
    e = Sub()

    a.print_num_instances()
    Sub.print_num_instances()
    Spam.print_num_instances()

    f = Other()

    f.print_num_instances()
    Spam.print_num_instances()

    a, b = SpamSecond(), SpamSecond()
    a.print_num_instances()                                         # В первом аргументе передается класс
    SpamSecond.print_num_instances()                                # Также в первом аргументе передается класс
