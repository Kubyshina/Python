"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, matrix_list):
        self.__matrix_list = matrix_list

    def __str__(self):
        matrix_string = ""
        for line in self.__matrix_list:
            matrix_string += str(line) + '\n'
        return matrix_string

    def __add__(self, other):
        result_list = self.__matrix_list
        for i in range (0, len(other.__matrix_list)):
            try:
                for j in range(0, len(other.__matrix_list[i])):
                    try:
                        result_list[i][j] += other.__matrix_list[i][j]
                    except IndexError:
                        result_list[i].append(other.__matrix_list[i][j])
            except IndexError:
                result_list.append(other.__matrix_list[i])
        return Matrix(result_list)


matrix1 = Matrix([[1, 2, 3, 8], [4, 5, 6], [1, 2, 3]])
matrix2 = Matrix([[6, 5, 4], [3, 2, 1, 0], [1, 2, 3], [1, 2, 5]])
print(matrix1)
print(matrix2)

print(matrix1 + matrix2)
