#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/26 11:33
# @Author: hongfei.shen
# @File  : multiplication_table.py

'''
输出乘法口诀表(九九表)
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()
