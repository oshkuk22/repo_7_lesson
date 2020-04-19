"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
 пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно. Для определения расхода ткани по каждому типу одежды
использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих
методов на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""


class Clothes:
    def __init__(self, type_clother, count_, size):
        self._type_clother = type_clother
        self._count_ = count_
        self._size = size


class Coast(Clothes):
    @property
    def count_coast(self):
        fabric_coast = self._count_ * (self._size / 6.5 + 0.5)
        return fabric_coast

class Costume(Clothes):
    @property
    def count_costume(self):
        fabric_costume = self._count_ * (self._size + 0.3)
        return fabric_costume


costume = Costume('costume', 5, 52)
coast = Coast('coast', 10, 48)

print(f'Count of fabric needed for sewing {costume._count_} '
      f'costumes {costume._size} size  and {coast._count_} coast {costume._size} size '
      f'equal {costume.count_costume+coast.count_coast:.3f} - m')

