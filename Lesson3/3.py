"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def my_func(num1, num2, num3):
    num_list = sorted([num1, num2, num3], reverse=True)
    return num_list[0]+num_list[1]


print(my_func(7, 2, 10))
