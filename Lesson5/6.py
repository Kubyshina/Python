"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести
словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

from re import findall

lessons_list = []
lessons_dict = {}

with open("6.txt", "r", encoding="utf-8") as file:
    lessons_list = file.readlines()

print(lessons_list)

for lesson in lessons_list:
    lessons_hours = 0
    lesson_name = lesson.split(":")[0]
    hours = findall("\d+",lesson)
    for hour in hours:
        lessons_hours += int(hour)
    lessons_dict[lesson_name] = lessons_hours

print(lessons_dict)
