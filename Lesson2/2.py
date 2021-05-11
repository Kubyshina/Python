# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

newList = []

while True:
    userInput = input("Введите любое значение. Для завершения нажмите Enter:\n")
    if len(userInput) > 0:
        newList.append(userInput)
    else:
        break

print(f"Список до сортировки: {newList}")

i = 0
while (i + 1) < len(newList):
    temp = newList[i]
    newList[i] = newList[i+1]
    newList[i+1] = temp
    i = i+2

print(f"Список после сортировки: {newList}")
