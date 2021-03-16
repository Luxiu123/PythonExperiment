# 1.	练习：人机对话：要求根据姓名、性别、年龄……分别提问及回答。


class Person:
    def __init__(self, name: str, sex: str, age: int):
        self.name = name
        self.sex = sex
        self.age = age


person = Person(input('请输入姓名：'), input('请输入性别：'), input('请输入年龄：'))
print(f"你的姓名是{person.name}, 性别是{person.sex}, 年龄是{person.age}")
