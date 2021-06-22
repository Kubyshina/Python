"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return ComplexNumber(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return ComplexNumber(new_a, new_b)

    def __str__(self):
        return f"z = {self.a} + {self.b}*i"


number1 = ComplexNumber(1, 2)
print(number1)
number2 = ComplexNumber(3, 4)
print(number2)
number3 = number1 + number2
print(number3)
number4 = number1 * number2
print(number4)
