"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

numbers = []
text_numbers = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("4.txt", "r", encoding="utf-8") as file:
    for string in file:
        numbers.append(string)

new_numbers = []

for string in numbers:
    for number in text_numbers.keys():
        if number in string:
            new_numbers.append(string.replace(number, text_numbers.get(number)))

print(new_numbers)

with open("41.txt", "a", encoding="utf-8") as file:
    file.writelines(new_numbers)
