"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

from re import findall
from json import dumps

firms_list = []
firms_dict = {}

with open("7.txt", "r", encoding="utf-8") as file:
    firms_list = file.readlines()


total_profit = 0
for firm in firms_list:
    profit = 0
    firm_name = firm.split()[0]
    numbers = firm.split()
    profit = int(numbers[2]) - int(numbers[3])
    total_profit += profit
    firms_dict[firm_name] = profit

firms_dict["average_profit"] = total_profit
firms_json = dumps(firms_dict)

with open("71.txt", "w", encoding="utf-8") as file:
    file.write(firms_json)
