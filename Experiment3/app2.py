# -*- coding:utf-8 -*-

def fib1(n: int):
    i1 = 1
    i2 = 1
    i3 = 2
    num_list = [1, 1]
    if n <= 0:
        raise ValueError("n less than or equal 0")
    if n == 1 or n == 2:
        return 1
    for i in range(2, n):
        i3 = i1 + i2
        i1 = i2
        i2 = i3
        num_list.append(i3)
    return i3, num_list


def fib2(n: int):
    if n <= 0:
        raise ValueError("n less than or equal 0")
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


def print_fib(arr: list):
    for i in range(2):
        for j in range(i * 10, (i + 1) * 10):
            print("%5d" % arr[j], end='')
        print()


if __name__ == '__main__':
    print_fib(fib1(20)[1])
    nums = []
    for i in range(1, 21):
        nums.append(fib2(i))
    print_fib(nums)
