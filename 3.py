"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
 В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
 В классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
 (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****"""


class Input_:
    def __init__(self, list_for_matrix):
        self.__list_matrix = list_for_matrix

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.__list_matrix)


class Cell:
    def __init__(self, count_in_cell):
        self._count_in_cell = count_in_cell

    def __add__(self, other):
        new_cell = self._count_in_cell + other._count_in_cell
        return new_cell

    def __sub__(self, other):
        new_cell = self._count_in_cell - other._count_in_cell
        if new_cell >= 0:
            return new_cell
        else:
            raise ValueError('Operation is not defined for these objects')

    def __mul__(self, other):
        new_cell = self._count_in_cell * other._count_in_cell
        return new_cell

    def __truediv__(self, other):
        if self._count_in_cell > other._count_in_cell:
            new_cell = self._count_in_cell // other._count_in_cell
        else:
            new_cell = other._count_in_cell // self._count_in_cell
        return new_cell

    def __gt__(self, other):
        return self._count_in_cell > other

    def __eq__(self, other):
        return  self._count_in_cell == other

    def __mod__(self, other):
        return self._count_in_cell % other

    def make_order(self, count_cell, count_columns):
        row_rows = []
        row = []
        self._count_cells = Cell(count_cell)
        if self._count_cells._count_in_cell > count_columns:
            for i in range(count_columns):
                row.append('*')
            for i in range(self._count_cells._count_in_cell // count_columns):
                row_rows.append(row)
            row = []
            for i in range(self._count_cells._count_in_cell % count_columns):
                row.append('*')
            row_rows.append(row)
        elif self._count_cells == count_columns:
            for i in range(count_columns):
                row_rows.append('*')
        else:
            for i in range(self._count_cells._count_in_cell):
                row_rows.append('*')
        return row_rows


cell_1 = Cell(10)
cell_2 = Cell(9)
print(cell_1 + cell_2)
print(cell_1 - cell_1)
print(cell_1 * cell_2)
print(cell_2 / cell_1)
print()
cell_1.make_order(5, 4)
c = Input_(cell_1.make_order(37, 9))
print(c)
# for pull_requests
