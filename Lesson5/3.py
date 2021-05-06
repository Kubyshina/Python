"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

emp_list = {}

with open("3.txt", "r", encoding="utf-8") as file:
    for file_content in file:
        employee = file_content.split()
        try:
            emp_list[employee[0]] = employee[1]
        except IndexError:
            break

print(emp_list)

low_salary = [employee for employee in emp_list.keys() if int(emp_list.get(employee)) < 20000]
print(low_salary)

total_salary = 0
for employee in emp_list.keys():
    total_salary += int(emp_list.get(employee))

average_salary = total_salary / len(emp_list)
print(average_salary)

