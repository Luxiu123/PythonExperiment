# -*- coding: UTF-8 -*-
class NamedTuple:
    def __init__(self, file: str) -> None:
        self.__file = file  # 文件路径
        self.__data = []  # 文件原数据
        self.__avg_arr = []  # 平均成绩数据

    def init(self):
        self.__data = self.read_csv()
        self.__avg_arr = self.get_avg_arr()

    def read_csv(self) -> list:
        """
        读取csv
        :return: list
        """
        src = ''
        with open(self.__file, encoding="utf-8") as f:
            src = f.read()
        data = [line.strip().split(",") for line in src.split("\n")]
        return data

    def __get_arr_avg(self, arr: list) -> float:
        """
        :param arr: student 元组
        :return: 语数外平均分
        """
        return sum([float(arr[1]), float(arr[2]), float(arr[3]), float(arr[4])]) / 4

    def get_avg_arr(self) -> list:
        """
        获取结果集
        :return: [[stu_id, avg]]
        """
        arr = []
        for stu in self.__data:
            arr.append([stu[0], self.__get_arr_avg(stu)])
        return arr

    def show(self):
        self.init()
        print("学号\t平均成绩")
        for stu in self.__avg_arr:
            print(stu[0], "%.2f" % stu[1])

    def __str__(self):
        self.show()


if __name__ == '__main__':
    NamedTuple("scores.csv").show()
