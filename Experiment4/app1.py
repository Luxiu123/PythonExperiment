# -*- coding=utf-8 -*-
from math import pi


class MyMath:
    def get_area(self):
        ...

    def print(self):
        ...


class Circle(MyMath):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.__radius

    def print(self):
        print("圆的周长 = {:.2f}".format(self.get_perimeter()))
        print("圆的面积 = {:.2f}".format(self.get_area()))


class Globe(MyMath):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return 4 * pi * self.__radius ** 2

    def get_volume(self):
        return (4 * pi * self.__radius ** 3) / 3

    def print(self):
        print("球的表面积 = {:.2f}".format(self.get_area()))
        print("球的体积 = {:.2f}".format(self.get_volume()))


if __name__ == "__main__":
    radius = 0
    try:
        radius = int(input("请输入半径："))
    except ValueError as e:
        print("输入有误")
    Circle(radius).print()
    Globe(radius).print()
