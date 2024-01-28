#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from abc import ABC, abstractmethod
import math


class Array(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def foreach(self):
        pass


class SortArray(Array):
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        if isinstance(other, SortArray):
            # Объединение множеств
            return SortArray(list(set(self.elements + other.elements)))
        else:
            raise TypeError("Неверный тип операнда")

    def foreach(self):
        # Сортировка элементов
        self.elements.sort()
        print(f"Отсортированный массив: {self.elements}")


class XorArray(Array):
    def __init__(self, elements):
        self.elements = elements

    def __add__(self, other):
        if isinstance(other, XorArray):
            # Исключающее ИЛИ
            xor_result = list(set(self.elements) ^ set(other.elements))
            return XorArray(xor_result)
        else:
            raise TypeError("Неверный тип операнда")

    def foreach(self):
        # Вычисление корня
        sqrt_elements = [math.sqrt(element) for element in self.elements]
        print(f"Массив корней: {sqrt_elements}")


if __name__ == "__main__":
    sort_array1 = SortArray([3, 1, 4, 1, 5, 9, 2])
    sort_array2 = SortArray([5, 6, 2, 7, 1, 8, 2])

    xor_array1 = XorArray([1, 2, 3, 4, 5])
    xor_array2 = XorArray([4, 5, 6, 7, 8])

    print("Сложение SortArray:")
    result_sort_array = sort_array1 + sort_array2
    result_sort_array.foreach()

    print("\nСложение XorArray:")
    result_xor_array = xor_array1 + xor_array2
    result_xor_array.foreach()
