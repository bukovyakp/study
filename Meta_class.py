# __author__ = 'pavel'

from sys import stdout as stdout

class Meta(object):
    """
    Методы метакласса. Напишите класс с именем Meta с методами, которые
    перехватывают все обращения к  атрибутам (как получение значения, так
    и присваивание) и выводят сообщения, перечисляющие их аргументы, на
    stdout. Создайте экземпляр класса Meta и поэкспериментируйте с ним в ин-
    терактивной оболочке. Что произойдет, если попытаться использовать эк-
    земпляр класса в  выражении? Попробуйте выполнить над своим классом
    операции сложения, доступа к  элементам по индексу и  получения среза.
    (Примечание: самый типичный способ, основанный на использовании __ge-
    tattr__, будет действовать в 2.6, но не будет в 3.0, по причинам, упомянутым
    в главе 30 и вновь приведенным в решении этого упражнения.)
    """
    def __getattr__(self, attr):
        print('Method __getattr__ get attribute: {0}'.format(attr))

    def __setattr__(self, attr, value):
        print('Method __setattr__ set attribute: {0}  -->  {1}'.format(attr, value))
        return object.__setattr__(self, attr, value)



if __name__ == '__main__':
    a = Meta()
    print(a.test_attr)
    a.test_attr = 'test'
    print(a.test_attr)
    print(a.test_attr[1:3])
