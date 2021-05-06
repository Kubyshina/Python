"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = [1, 2, 5, 10, 12]

with open("5.txt", "w", encoding="ascii") as file:
    for number in numbers:
        file.write(F"{number} ")

summa = 0
with open("5.txt", "r", encoding="ascii") as file:
    for file_content in file:
        nums = file_content.split()
        for number in nums:
            summa += int(number)

print(summa)