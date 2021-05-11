"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу
метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    _length_ = 0
    _width_ = 0

    def __init__(self, length, width):
        self._length_ = length
        self._width_ = width

    def asphalt_amount(self, weight, depth):
        amount = self._length_ * self._width_ * weight * depth
        print(amount)


new_road = Road(50, 10)
new_road.asphalt_amount(1, 5)

