# -*- coding: UTF-8 -*-
from math import pi


class AreaVolume:
    def get_area(self, radius):
        ...


class Circle(AreaVolume):
    def __init__(self, r) -> None:
        self.__r = r

    def get_area(self, radius):
        return pi * radius ** 2

    def __str__(self) -> str:
        return "圆的面积 = {:.2f}".format(self.get_area(self.__r))


class Globe(AreaVolume):
    def __init__(self, r) -> None:
        self.__r = r

    def get_area(self, radius):
        return (4 * pi * radius ** 3) / 3

    def __str__(self) -> str:
        return "球体体积 = {:.2f}".format(self.get_area(self.__r))


if __name__ == '__main__':
    r = input("请输入半径：")
    try:
        r = float(r)
        print(Circle(r))
        print(Globe(r))
    except ValueError as e:
        print(e)
