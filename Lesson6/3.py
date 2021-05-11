"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    wage = 0
    bonus = 0
    _income = {"wage": wage, "bonus": bonus}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(self.wage + self.bonus)


position = Position("Вася", "Пупкин", "менеджер", 10000, 2000)
position.get_full_name()
position.get_total_income()
