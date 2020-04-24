# encoding: utf-8
"""
@version: 1.0
@author: 
@file: VariableScope
@time: 2020-03-18 15:59
"""

""" 变量作用域"""


def foo():
    b = "hello"
    global a
    a = 200

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()


if __name__ == "__main__":
    # a = 100
    foo()
    print(a)
