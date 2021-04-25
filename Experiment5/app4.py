# -*- coding: UTF-8 -*-
import sys


def args():
    arg_list = sys.argv
    print(f"参数个数 = {len(arg_list)}")
    for index, arg in enumerate(arg_list):
        print(f"sys.argv[{index}] = {arg}")


if __name__ == '__main__':
    args()
