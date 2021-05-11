"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Скорость {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    is_police = True


town_car1 = TownCar(50, "black", "Alice")
print(f"{town_car1.speed} {town_car1.name} {town_car1.color} {town_car1.is_police}")
town_car1.show_speed()
town_car1.go()
town_car1.stop()
town_car1.turn("налево")

town_car2 = TownCar(70, "green", "Bob")
print(f"{town_car2.speed} {town_car2.name} {town_car2.color} {town_car2.is_police}")
town_car2.show_speed()
town_car2.go()
town_car2.stop()
town_car2.turn("направо")

sport_car = SportCar(150, "red", "Super")
print(f"{sport_car.speed} {sport_car.name} {sport_car.color} {sport_car.is_police}")
sport_car.show_speed()
sport_car.go()
sport_car.stop()
sport_car.turn("направо")

work_car1 = WorkCar(150, "white", "Crazy")
print(f"{work_car1.speed} {work_car1.name} {work_car1.color} {work_car1.is_police}")
work_car1.show_speed()
work_car1.go()
work_car1.stop()
work_car1.turn("налево")

work_car2 = WorkCar(30, "white", "Crazy")
print(f"{work_car2.speed} {work_car2.name} {work_car2.color} {work_car2.is_police}")
work_car2.show_speed()
work_car2.go()
work_car2.stop()
work_car2.turn("налево")

police_car = PoliceCar(30, "blue", "Police")
print(f"{police_car.speed} {police_car.name} {police_car.color} {police_car.is_police}")
police_car.show_speed()
police_car.go()
police_car.stop()
police_car.turn("налево")