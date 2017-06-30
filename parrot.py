# __author__ = 'pavel'
# coding: utf-8

"""
Напишите набор классов на языке Python, которые
реализовали бы эту схему средствами композиции. Класс Scene (сцена)
должен определять метод action и  встраивать в  себя экземпляры классов
Customer (клиент), Clerk (клерк) и Parrot (попугай), каждый из которых должен
определять метод line, выводящий уникальное сообщение. Встраива-
емые объекты могут наследовать один общий суперкласс, определяющий
метод line, который просто выводит текст указанного ему сообщения, или
определяют собственные реализации метода line.

"""

class Customer:
    def line(self):
        print('that’s one ex-bird!')

class Clerk:
    def line(self):
        print('no it isn’t...')

class Parrot:
    def line(self):
        self.message = None
        print(self.message)

class Scene:
    def action(self):
        self.caustomer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()

        self.caustomer.line()
        self.clerk.line()
        self.parrot.line()

if __name__ == '__main__':
    Scene().action()

