# -*- coding=utf-8 -*-
class Color:
    def __init__(self, r=0, g=0, b=0):
        self._r = r
        self._g = g
        self._b = b

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    def luminance(self):
        return .299 * self._r + .587 * self._g + .114 * self._b

    def to_gray(self):
        y = int(round(self.luminance()))
        return Color(y, y, y)

    def is_compatible(self, c):
        return abs(self.luminance() - c.luminance()) > 128.0

    def __str__(self):
        return f"({self._r},{self._g},{self._b})"


WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
RED = Color(0, 255, 0)
if __name__ == '__main__':
    c = Color(255, 200, 0)
    print(f"颜色字符串:{c}")
    print(f"颜色分量:r = {c.r}, g = {c.g}, b = {c.g}")
    print(f"颜色亮度:{c.luminance()}")
    print(f"转换为灰度颜色:{c.to_gray()}")
    print(f"{c}和{RED}是否匹配:{c.is_compatible(RED)}")
