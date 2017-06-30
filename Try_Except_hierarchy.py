# coding: utf-8

def action2():
    print(1 + [])               # Возбуждает исключение TypeError


def action1():
    try:
        action2()
    except TypeError:           # Самая последняя соответствующая инструкция try
        print('inner try')


if __name__ == '__main__':
    try:
        action1()
    except TypeError:           # Этот обработчик будет выполнен, только если
        print('outer try')      # action1 повторно возбудит исключение

# Иерархия в конструкции finally
# исключение пройдет через все блоки finally независимо от того,
# вложены они синтаксически или в ходе выполнения программы
# происходит вложение физически отдельных фрагментов программного кода:

    try:
        try:
            raise IndexError
        finally:
            print('spam')
    finally:
        print('SPAM')

