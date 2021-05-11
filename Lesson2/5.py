# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rateList = []

while True:
    userInput = input("Введите число или нажмите Enter для завершения:\n")
    if len(userInput) == 0:
        break

    if userInput.isdigit():
        number = int(userInput)
        if len(rateList) == 0:
            rateList.append(number)
        elif len(rateList) == 1:
            if rateList[0] >= number:
                rateList.insert(1, number)
            else:
                rateList.insert(0, number)
        else:
            for el in rateList:
                if el < number and (rateList.index(el) == 0 or rateList[rateList.index(el)-1] >= number):
                    rateList.insert(rateList.index(el), number)
                    break
                elif rateList.index(el) == len(rateList) - 1:
                    rateList.insert(rateList.index(el)+1, number)
                    break
        print(rateList)
