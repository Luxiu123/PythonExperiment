# 3.  编写一个猜年龄的小游戏。
print("==========猜年龄游戏==========")
answer = 21
while True:
    age = input("请输入年龄：")
    try:
        age = int(age)
        if age > answer:
            print('猜大了！')
        elif age < answer:
            print('猜小了！')
        else:
            print('猜中了')
            break

    except Exception as e:
        print(e)