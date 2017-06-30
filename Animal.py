# __author__ = 'pavel'
# coding: utf-8

class Animal:
    def reply(self):
        self.speak()

class Mammal(Animal):
    def speak(self):
        print('Some sound')

class Cat(Mammal):
    def speak(self):
        print('Mauuu BLYA')

class Dog(Mammal):
    def speak(self):
        print('Ay-y-y-y-y-y')

class Primate(Mammal):
    def speak(self):
        print('UUUUUUUU')

class Hacker(Primate): pass
    # def speak(self):
    #    print('Fuck the system, bitch')


if __name__ == '__main__':
    spot = Cat()
    spot.reply()

    hak = Hacker()
    hak.reply()