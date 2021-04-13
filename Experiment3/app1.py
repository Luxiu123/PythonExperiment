# -*- coding:utf-8 -*-

def fact1(n: int):
    if n < 0:
        raise ValueError("n less than 0")
    if n == 0:
        return 1
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def fact2(n: int):
    if n < 0:
        raise ValueError("n less than 0")
    if n == 0:
        return 1
    return n * fact2(n - 1)


if __name__ == '__main__':
    i = input("输入一个整数：")
    try:
        i = int(i)
        print(f"{i}! = {fact1(i)}")
        print(f"{i}! = {fact2(i)}")
    except ValueError as e:
        print(e)
