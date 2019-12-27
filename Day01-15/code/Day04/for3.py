#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/26 11:42
# @Author: hongfei.shen
# @File  : for3.py
'''
输入非负整数n计算n!
'''
n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
