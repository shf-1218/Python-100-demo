#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/26 11:45
# @Author: hongfei.shen
# @File  : for4.py
'''
输入一个正整数判断它是不是素数
'''
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(1, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
