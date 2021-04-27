# -*- coding: UTF-8 -*-

import json
import os

ab = {}
if os.path.exists("addressbook.json"):
    with open("addressbook.json", "r", encoding="utf-8") as f:
        ab = json.load(f)
while True:
    print("|---欢迎使用通讯录程序---|")
    print("|---1：显示通讯录清单---|")
    print("|---2：查询联系人资料---|")
    print("|---3：插入新的联系人---|")
    print("|---4：删除已有联系人---|")
    print("|---0：退出---|")
    choice = input("请使用功能菜单(0-4):").strip()
    if choice == '1':
        if len(ab) == 0:
            print("通讯录为空")
        else:
            for k, v in ab.items():
                print(f"姓名 = {k}，联系电话 = {v}")
    elif choice == '2':
        name = input("请输入联系人姓名：")
        if name not in ab:
            ask = input("联系人不存在，是否增加用户资料(Y/N)")
            if ask in ["Y", 'y']:
                tel = input("请输入用户联系电话：")
                ab[name] = tel
        else:
            print(f"联系人信息：{name} {ab[name]}")
    elif choice == '3':
        name = input("请输入联系人姓名：")
        if name in ab:
            print(f"已存在联系人：{name} {ab[name]}")
            ask = input("是否修改用户资料(Y/N)")
            if ask in ["Y", 'y']:
                tel = input("请输入用户联系电话：")
                ab[name] = tel
        else:
            tel = input("请输入用户联系电话：")
            ab[name] = tel
    elif choice == '4':
        name = input("请输入联系人姓名：")
        if name not in ab:
            print(f"联系人不存在：{name}")
        else:
            tel = ab.pop(name)
            print(f"删除联系人：{name} {tel}")
    elif choice == '0':
        with open("addressbook.json", "w", encoding="utf-8") as f:
            json.dump(ab, f)
        break
