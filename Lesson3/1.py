"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func(dividend, divisor):
    try:
        result = int(dividend) / int(divisor)
        return result
    except ZeroDivisionError:
        return "Ошибка: нельзя делить на ноль!"
    except ValueError:
        return "Введены некорректные значения"


arg1 = input("Введите делимое:\n")
arg2 = input("Введите делитель:\n")
print(my_func(arg1, arg2))
