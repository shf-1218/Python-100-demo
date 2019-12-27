#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/26 14:54
# @Author: hongfei.shen
# @File  : for6.py
'''
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''

num = int(input('请输入打印行数: '))

for x in range(num):
    for y in range(x + 1):
        print('*', end='')
    print()

for x in range(num):
    for y in range(num):
        if y < num - x - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for x in range(num):
    for y in range(num):
        if y < num - x - 1:
            print(' ', end='')
    for j in range(2 * x + 1):
        print('*', end='')
    print()
