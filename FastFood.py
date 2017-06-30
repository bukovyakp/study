# __author__ = 'pavel'
# coding: utf-8


class Lunch:
    def __init__(self):                                     # Создает и встраивает Customer и Employee
        self.customer = Customer()
        self.employee = Employee()                          # Действующее лицо, принимающее заказ
        self.order()

    def order(self, food_name):                             # Имитирует прием заказа
        Customer.place_order(food_name, self.employee)

    def result(self):                                       # Запрашивает у клиента название блюда
        pass


class Customer:
    def __init__(self):                                     # Инициализирует название блюда значением None
        Food.food_name = None

    def place_order(self, food_name, employee):             # Передает заказ официанту
        Employee.take_order(food_name)
        self.customer = employee

    def print_food(self):                                   # Выводит название блюда
        print(Food.food_name)


class Employee:
    def take_order(self, food_name):                         # Возвращает блюдо с указанным названием
        Food.food_name = food_name
        print(food_name)


class Food:
    def __init__(self, name):                               # Сохраняет название блюда
        self.food_name = name


if __name__ == '__main__':
    a = Employee()
    a.take_order('potates')
    print(Food.food_name)
