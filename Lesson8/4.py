"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class StoreHouse:
    pass


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


printer = Printer()
printer.ping()
printer.print()

scanner = Scanner()
scanner.ping()
scanner.scan()

xerox = Xerox()
xerox.ping()
xerox.copy(3)
