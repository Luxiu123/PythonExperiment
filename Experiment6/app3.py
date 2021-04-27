# -*- coding: UTF-8 -*-
# 归并排序
def merge(left, right):
    merged = []
    i, j = 0, 0
    left_len, right_len = len(left), len(right)
    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


if __name__ == '__main__':
    a = [12, 423, 24, 234, 56, 23, 93, 2, 21]
    a1 = merge_sort(a)
    print(a1)
