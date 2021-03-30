# -*- coding: UTF-8 -*-
# 输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理。
num1 = input("输入第一个整数：")
num2 = input("输入第二个整数：")
status = False
try:
    if num1.find('.') == -1 and num2.find('.') == -1:
        num1 = int(num1)
        num2 = int(num2)
        if num2 != 0:
            status = True
            print(num1 / num2)
except Exception as e:
    print(e)
        
if not status:
    raise Exception("不是整数或除数为0")
