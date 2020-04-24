# encoding: utf-8
"""
@version: 1.0
@author: 
@file: Read
@time: 2020-03-29 22:10
"""


def read_one():
    f = None
    try:
        # 一次性读取整个文件内容
        f = open("./imei.txt", 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def read_two():
    f = None
    try:
        # 一次性读取整个文件内容
        with open("./imei.txt", 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


import time


def read_three():
    # 通过for-in循环逐行读取
    with open('./imei.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            # time.sleep(0.5)


def read_four():
    # 读取文件按行读取到列表中
    with open('./imei.txt', 'r') as f:
        lines = f.readlines()
    print(lines)


if __name__ == "__main__":
    # read_one()
    # read_two()
    # read_three()
    read_four()
