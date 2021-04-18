# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

value = input("Enter the number:\n")

while not value.isdigit():
    value = input("Input must be a number:\n")

result = int(value) + int(value+value) + int(value+value+value)
print(result)
