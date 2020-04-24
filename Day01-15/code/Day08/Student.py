# encoding: utf-8
"""
@version: 1.0
@author: 
@file: Student
@time: 2020-03-29 16:10
"""


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


class Test(object):
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


# def main():
#     # 创建学生对象并指定姓名和年龄
#     stu1 = Student('骆昊', 38)
#     # 给对象发study消息
#     stu1.study("Python程序设计")
#     # 给对象发watch_av消息
#     stu1.watch_movie()
#     stu2 = Student('王大锤', 15)
#     stu2.study('思想品德')
#     stu2.watch_movie()


# def main():
#     test = Test('hello')
#     # AttributeError: 'Test' object has no attribute '__bar'
#     test.__bar()
#     # AttributeError: 'Test' object has no attribute '__foo'
#     print(test.__foo)


def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == '__main__':
    main()
