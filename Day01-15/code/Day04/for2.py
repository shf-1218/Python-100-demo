#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/26 11:19
# @Author: hongfei.shen
# @File  : for2.py
'''
用for循环实现1~100之间的偶数求和
'''

sum = 0
for x in range(0, 101, 2):
    sum += x
print('1~100之间的偶数之和', sum)

'''
在循环中使用分支结构实现1~100之间的偶数求和
'''
sum = 0
for x in range(101):
    if x % 2 == 0:
        sum += x
print('1~100之间的偶数之和', sum)
