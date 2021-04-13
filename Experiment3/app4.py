# -*- coding:utf-8 -*-

def fun(arr: list):
    if not arr:
        return None, None, 0
    max_num = arr[0]
    min_num = arr[0]
    length = len(arr)
    for i in arr:
        if max_num < i:
            max_num = i
        if min_num > i:
            min_num = i
    return max_num, min_num, length


if __name__ == '__main__':
    arr = [1, 2, 23, -10.3, 7, 36]
    r = fun(arr)
    print(f"最大值:{r[0]}, 最小值:{r[1]}，元素个数:{r[2]}")
