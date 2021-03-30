# -*- coding: UTF-8 -*-
# ①、普通年能被4整除且不能被100整除的为闰年。（如2004年就是闰年,1901年不是闰年）
# ②、世纪年能被400整除的是闰年。(如2000年是闰年，1900年不是闰年)

year = input("输入年份：")
status = False
try:
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        status = True
    if year % 100 == 0 and year % 400 == 0:
        status = True
    if status:
        print("是闰年")
    else:
        print("不是闰年")
except Exception as e:
    print(e)
