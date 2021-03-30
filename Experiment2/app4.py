# -*- coding: UTF-8 -*-
# 利用下面的计算公式计算e的近似值，要求最后一项小于10-6

def get_e():
    result = 0
    precision = 1e-06
    n = 1
    while 1 / rank(n) > precision:
        result += 1 / rank(n)
        n += 1
    return result


def rank(n):
    if n == 0:
        return 1
    elif n > 0:
        num = 1
        for i in range(1, n + 1):
            num *= i
        return num
    else:
        raise Exception("n < 0")


print(get_e())
