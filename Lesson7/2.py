"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import abstractmethod


class Clothes:

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size: int):
        self.size = size

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Dress(Clothes):

    def __init__(self, height: int):
        self.height = height

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 1)


coat = Coat(13)
print(coat.fabric_consumption)

dress = Dress(180)
print(dress.fabric_consumption)
