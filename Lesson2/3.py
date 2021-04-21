# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

userInput = input("Введите номер месяца в виде целого числа от 1 до 12:\n")

if userInput.isdigit():
    month = int(userInput)

    print("Первый  вариант (список)")
    winter = [12, 1, 2]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if month in winter:
        print(f"{month} месяц - зима")
    elif month in spring:
        print(f"{month} месяц - весна")
    elif month in summer:
        print(f"{month} месяц - лето")
    elif month in autumn:
        print(f"{month} месяц - осень")
    else:
        print("Месяца с таким номером не существует")

    print("<---------->")
    print("Второй вариант (словарь)")
    monthDict = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
                 10: "осень", 11: "осень", 12: "зима"}

    if 0 < month <= 12:
        print(f"{month} месяц - это {monthDict.get(month)}")
    else:
        print("Месяца с таким номером не существует")
else:
    print("Вы ввели не число")
