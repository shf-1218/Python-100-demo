# encoding: utf-8
"""
@version: 1.0
@author: 
@file: module3
@time: 2020-03-18 15:24
"""

def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()