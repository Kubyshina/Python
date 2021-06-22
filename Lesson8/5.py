"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""
import abc


class StoreHouse:
    __equipmentList = {}

    @classmethod
    def reception(cls, equipment):
        if equipment.__name__ in cls.__equipmentList.keys():
            cls.__equipmentList[equipment.__name__] += 1
        else:
            cls.__equipmentList[equipment.__name__] =1

    @classmethod
    def delivery(cls, equipment):
        if equipment.__name__ in cls.__equipmentList.keys() and cls.__equipmentList[equipment.__name__] > 0:
            cls.__equipmentList[equipment.__name__] -= 1
        else:
            print("Такого оборудования нет на складе")

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


StoreHouse.reception(Printer)
StoreHouse.reception(Printer)
StoreHouse.reception(Scanner)
StoreHouse.reception(Scanner)
StoreHouse.reception(Xerox)
StoreHouse.reception(Printer)

StoreHouse.get_equipment()

StoreHouse.delivery(Printer)
StoreHouse.delivery(Scanner)
StoreHouse.delivery(Xerox)

StoreHouse.get_equipment()

StoreHouse.delivery(Xerox)

StoreHouse.get_equipment()
