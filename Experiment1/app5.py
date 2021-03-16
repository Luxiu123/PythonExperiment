# 5.输入直角三角形两直角边a,b求斜边C,并输出。(from math import *)

import cmath

input_string = input('输入直角三角形两斜边(用,分隔):')
a, b = input_string.split(',')
c = 0
try:
    a = int(a)
    b = int(b)
    c = cmath.sqrt(a**2 + b**2).real
except Exception as e:
    print(e)
print(f'结果为{c}')