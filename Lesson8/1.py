"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import datetime


class Date:

    @classmethod
    def get_date(cls, new_date):
        try:
            if cls.validate_date(new_date):
                date_array = new_date.split("-")
                return datetime.date(int(date_array[2]), int(date_array[1]), int(date_array[0]))
            else:
                return "Не удалось преобразовать дату"
        except:
            return "Не удалось преобразовать дату"

    @staticmethod
    def validate_date(new_date):
        try:
            date_array = new_date.split("-")
            number = int(date_array[0])
            if number < 1 or number > 31:
                return False
            month = int(date_array[1])
            if month < 1 or number > 12:
                return False
            year = int(date_array[2])
            if year < 1900 or year > 2100:
                return False
            return True
        except:
            return False


print(Date.validate_date("1-2-3"))
print(Date.validate_date("1-2-1990"))

print(Date.get_date("1-2-3"))
print(Date.get_date("1-2-1990"))
