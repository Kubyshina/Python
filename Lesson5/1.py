"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

while True:
    with open("1.txt", "a", encoding="utf-8") as file:
        user_input = input("Введите данные для записи в файл:\n")
        if len(user_input) == 0:
            break
        else:
            file.write(f"{user_input}\n")
