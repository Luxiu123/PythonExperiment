# 6.编写程序，输入球的半径，计算球的表面积和体积，半径为实数，
# 用π，结果输出为浮点数，共10位其中2位有效数字。
import math
import sys
r = input("输入球半径：")


def get_area(r):
    return math.pi * 4 * r**2


def get_volumn(r):
    return 4 / 3 * math.pi * r**3


try:
    r = float(r)
    print("表面积：{:.2f}".format(get_area(r)))
    print("体积：{:.2f}".format(get_volumn(r)))
except Exception as e:
    print(r)
