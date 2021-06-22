"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""
import abc


class StoreHouse:
    __equipmentList = {}

    @classmethod
    def reception(cls, equipment, number=1):
        try:
            number = int(number)
            cls.__equipmentList[equipment.__name__] += number
        except ValueError:
            print("Количество техники должно быть числом")
        except KeyError:
            cls.__equipmentList[equipment.__name__] = number

    @classmethod
    def delivery(cls, equipment, number=1):
        try:
            number = int(number)
            if cls.__equipmentList[equipment.__name__] - number >= 0:
                cls.__equipmentList[equipment.__name__] -= number
            else:
                print("Нужного оборудования нет на складе")
        except ValueError:
            print("Количество техники должно быть числом")
        except KeyError:
            print("Нужного оборудования нет на складе")


    @classmethod
    def get_equipment(cls):
        print(cls.__equipmentList)


class OfficeEquipment:
    def ping(self):
        print("Connection established.")


class Printer(OfficeEquipment):
    def print(self):
        print("Printing")


class Scanner(OfficeEquipment):
    def scan(self):
        print("Scanning")


class Xerox(OfficeEquipment):
    def copy(self, copies):
        for i in range(0, copies):
            print("Copying")


StoreHouse.delivery(Xerox)
StoreHouse.get_equipment()

StoreHouse.reception(Printer, "f")
StoreHouse.reception(Printer, 3)
StoreHouse.reception(Scanner)
StoreHouse.reception(Scanner)
StoreHouse.reception(Xerox)
StoreHouse.reception(Printer)
StoreHouse.get_equipment()

StoreHouse.delivery(Printer, 2)
StoreHouse.delivery(Scanner, "f")
StoreHouse.delivery(Scanner)
StoreHouse.delivery(Xerox)
StoreHouse.get_equipment()

StoreHouse.delivery(Xerox)
StoreHouse.get_equipment()
