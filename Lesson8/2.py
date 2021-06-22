"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class NullDivisionException(Exception):

    def __init__(self):
        print("Деление на ноль запрещено!")


try:
    number1 = int(input("Введите делимое"))
    number2 = int(input("Введите делитель"))
    if number2 == 0:
        raise NullDivisionException
except NullDivisionException as exception:
    print(exception)
except Exception as exception:
    print(exception)
else:
    print(number1/number2)
