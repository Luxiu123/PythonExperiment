# -*- coding=utf-8 -*-

import random
import math


class Stat:
    def __init__(self, n):
        self._data = []
        for i in range(n):
            self._data.append(0)

    def add_data_point(self, i):
        self._data[i] += 1

    def count(self):
        return sum(self._data)

    def mean(self):
        return sum(self._data) / len(self._data)

    def max(self):
        return max(self._data)

    def min(self):
        return min(self._data)

    def draw(self):
        for i in self._data:
            print("#" * i)


if __name__ == '__main__':
    st = Stat(10)
    for i in range(100):
        score = random.randrange(0, 10)
        st.add_data_point(math.floor(score))
    print(f"数据点个数{st.count()}")
    print(f"数据点个数的平均值{st.mean()}")
    print(f"数据点个数的最大值{st.max()}")
    print(f"数据点个数的最小值{st.min()}")
    st.draw()
