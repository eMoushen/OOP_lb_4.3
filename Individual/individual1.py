#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Triad:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def increase_fields(self):
        self.a += 1
        self.b += 1
        self.c += 1


class MyTime(Triad):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute, second)

    def increase_fields(self):
        super().increase_fields()

    def increase_seconds(self, n):
        self.c += n
        self.b += self.c // 60
        self.c %= 60
        self.a += self.b // 60
        self.b %= 60

    def increase_minutes(self, n):
        self.b += n
        self.a += self.b // 60
        self.b %= 60


if __name__ == "__main__":
    # Создаем объекты класса Triad
    triad = Triad(1, 2, 3)
    print(f"Тройка чисел: {triad.a}, {triad.b}, {triad.c}")

    my_time = MyTime(10, 25, 40)
    print(f"Время: {my_time.a} часов, {my_time.b} минут, {my_time.c} секунд")

    # Увеличение полей на 1
    triad.increase_fields()
    my_time.increase_fields()

    print(f"Тройка чисел: {triad.a}, {triad.b}, {triad.c}")
    print(f"Время: {my_time.a} часов, {my_time.b} минут, {my_time.c} секунд")

    # Увеличиваем время на 70 секунд
    my_time.increase_seconds(70)
    print(f"Время: {my_time.a} часов, {my_time.b} минут, {my_time.c} секунд")
