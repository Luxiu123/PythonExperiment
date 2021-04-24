# -*- coding=utf-8 -*-

class Temperature:
    def __init__(self, degree):
        self.__degree = degree

    def to_fahrenheit(self):
        return 32 + 1.8 * self.__degree

    def to_celsius(self):
        return (self.__degree - 32) / 1.8


if __name__ == "__main__":
    degree = 0
    try:
        degree = float(input("请输入摄氏温度："))
    except ValueError as e:
        print("输入有误")
    print("摄氏温度 = {:.1f}，华氏温度 = {:.1f}".format(degree, Temperature(degree).to_fahrenheit()))
    degree = 0
    try:
        degree = float(input("请输入华氏温度："))
    except ValueError as e:
        print("输入有误")
    print("摄氏温度 = {:.1f}，华氏温度 = {:.1f}".format(Temperature(degree).to_celsius(), degree))
