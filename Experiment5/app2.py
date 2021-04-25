# -*- coding: UTF-8 -*-
import re


class MyMyth:
    def add(self, a, b):
        ...

    def sub(self, a, b):
        ...

    def multiply(self, a, b):
        ...

    def div(self, a, b):
        ...

    def pow(self, a, b):
        ...


class Calculator(MyMyth):

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def pow(self, a, b):
        return a ** b


def parse_input(string: str):
    return re.split(r"\s+", string.strip())


if __name__ == '__main__':
    string = input("请输入两个数字，以空格分隔:")
    a, b = parse_input(string)
    cal = Calculator()
    try:
        a = float(a)
        b = float(b)
        print(f"{a} + {b} = {cal.add(a, b)}")
        print(f"{a} - {b} = {cal.sub(a, b)}")
        print(f"{a} * {b} = {cal.multiply(a, b)}")
        print(f"{a} / {b} = {cal.div(a, b)}")
        print(f"{a} ** {b} = {cal.pow(a, b)}")
    except ValueError as e:
        print(e)
