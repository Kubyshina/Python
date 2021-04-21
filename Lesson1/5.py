# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

inputValue = input("Введите выручку:\n")
while not inputValue.isdigit():
    inputValue = input("Выручка должна быть числом:\n")
proceeds = float(inputValue)

inputValue = input("Введите издержки:\n")
while not inputValue.isdigit():
    inputValue = input("Издержки должны быть числом:\n")
costs = float(inputValue)

if proceeds > costs:
    print("Финансовый результат: прибыль")
    profit = proceeds-costs
    print(f"Рентабельность: {(profit / proceeds):.2f}")
    inputValue = input("Введите численность сотрудников:\n")
    while not inputValue.isdigit():
        inputValue = input("Численность сотрудников должна быть числом:\n")
    employees = int(inputValue)
    print(f"Прибыль в расчёте на одного сотрудника: {(profit / employees):.2f}")
elif proceeds == costs:
    print("Финансовый результат: точка безубыточности")
else:
    print("Финансовый результат: убыток")
