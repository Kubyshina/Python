# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

value = input("Enter the time in seconds:\n")

while not value.isdigit():
    value = input("Input must be a number:\n")

time = int(value)
seconds = time % 60
minutes = time // 60 % 60
hours = time // 3600

print(f"Your time is: {hours}:{minutes}:{seconds}")
