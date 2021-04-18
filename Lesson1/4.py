# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

value = input("Enter the number:\n")

while not value.isdigit():
    value = input("Input must be a number:\n")

value = int(value)
result = 0
while value % 10 > 0:
    if result < value % 10:
        result = value % 10
    value = value // 10

print(result)
