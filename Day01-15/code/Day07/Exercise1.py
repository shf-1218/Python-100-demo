# encoding: utf-8
"""
@version: 1.0
@author: 
@file: Exercise1
@time: 2020-03-29 15:42
"""

import os
import time


def main():
    content = "北京欢迎你为你开天辟地…………"
    while True:
        os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
