"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import cycle
from sys import argv
script_name, numbers_count = argv

numbers = ["раз", "два", "три"]
try:
    i = 0
    for element in cycle(numbers):
        print(element)
        i += 1
        if i == int(numbers_count):
            break
except ValueError:
    print("Ошибка при обработке параметров")
