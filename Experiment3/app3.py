# -*- coding:utf-8 -*-

def min_n(a, b, *c):
    min_num = a if a < b else b
    for i in c:
        if min_num > i:
            min_num = i
    return min_num


if __name__ == '__main__':
    print(f"最小值为：{min_n(10, 25, -10, 20, 13.3)}")
