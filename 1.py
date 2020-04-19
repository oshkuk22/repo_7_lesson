"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д."""


class Matrix:
    def __init__(self, list_for_matrix):
        self.__list_matrix = list_for_matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.__list_matrix)

    def __add__(self, other):
        result = []
        numbers = []
        if len(self.__list_matrix) == len(other.__list_matrix):
            for i in range(len(self.__list_matrix)):
                if len(self.__list_matrix[i]) == len(other.__list_matrix[i]):
                    for j in range(len(self.__list_matrix[0])):
                        sum_ = other.__list_matrix[i][j] + self.__list_matrix[i][j]
                        numbers.append(sum_)
                    result.append(numbers)
                    numbers = []
                else:
                    raise TypeError('Can not add matrix of these dimensions')
            return Matrix(result)
        else:
            raise TypeError('Can not add matrix of these dimensions')


matrix_1 = Matrix([[1, 2, 3], [10, 23, 6], [7, 8, 2], [5, 8, 12]])
matrix_2 = Matrix([[5, 4, 2], [9, 2, 16], [1, 3, 2], [8, 9, 2]])
print(matrix_1)
print('\n\t+\n')
print(matrix_2)
print('\n\t=\n')
c = matrix_1+matrix_2
print(c)
