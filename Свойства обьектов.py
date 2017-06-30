__author__ = 'pavel'


# использование свойства в стандартном виде attribute = property(fget, fset, fdel, doc)
"""
class PropSquare:
    def __init__(self, start):
        self.value = start

    def getX(self):                 # Операция получения атрибута
        return self.value ** 2

    def setX(self, value):
        self.value = value

    X = property(getX, setX)

# Операция присваивания значения атрибуту
# Операция удаления не поддерживается,
# описание отсутствует

P = PropSquare(3)
Q = PropSquare(32)                  # 2 экземпляра класса со свойством
                                    # Каждый хранит собственное значение
print(P.X)  # 3 ** 2
P.X = 4
print(P.X)  # 4 ** 2
print(Q.X)  # 32 ** 2

"""

# Использование декоратора

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):                 # name = property(name)
        """name property docs"""
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):          # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):                 # name = name.deleter(name)
        print('remove...')
        del self._name

bob = Person('Bob Smith')           # Объект bob имеет управляемый атрибут
print(bob.name)                     # Вызовет метод getter свойства name (name 1)
bob.name = 'Robert Smith'           # Вызовет метод setter свойства name (name 2)
print(bob.name)
del bob.name                        # Вызовет метод deleter свойства name (name 3)
print('-'*20)
sue = Person('Sue Jones')           # Объект sue также наследует свойство
print(sue.name)
print(Person.name.__doc__)          # Или: help(Person.name)







